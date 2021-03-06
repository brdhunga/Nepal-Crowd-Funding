from datetime import date
from dateutil.relativedelta import relativedelta

import django
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, reverse_lazy
from django.test import tag

from .models import Project, Reward


class ProjectHomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.proj1 = Project(funding_goal=90000.00, 
            title="Test title 1", tagline="The best project",
            location="Kathmandu", description="Project description",
            )
        
        six_months = date.today() + relativedelta(months=+6)
        self.six_months = six_months
        user = User(username="test_user")
        user.set_password('usausausa')
        user.save()
        self.user = user
        
        self.proj2 = Project(funding_goal=90000.00, 
            title="Test title 1", tagline="The best project",
            location="Kathmandu", description="Project description",
            end_date = six_months, created_by = user
            )
        self.proj2.save()

        self.proj2_duplicate = Project(funding_goal=90000.00, 
            title="Test title 1", tagline="The best project",
            location="Kathmandu", description="Project description",
            end_date = six_months, created_by = user
            )
        self.proj2_duplicate.save()

        self.public_project = Project(funding_goal=90000.00, 
            title="Test title 1", tagline="The best project",
            location="Kathmandu", description="Project description",
            end_date = six_months, created_by = user,
            project_status = Project.ACTIVE
        )
        self.public_project.save()

        self.public_project_active = self.public_project
        self.public_project_active.project_status = Project.ACTIVE
        self.public_project_active.save()


    def test_cannot_save_without_user(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            self.proj1.save()

    def test_saves_project_with_no_error(self):
        self.assertEqual(self.proj2.project_status, Project.DRAFTED)

    def test_slug_not_empty(self):
        self.assertEqual(self.proj2.slug, "test-title-1")

    def test_slugs_are_unique(self):
        self.assertNotEqual(self.proj2.slug, self.proj2_duplicate.slug)

    def test_all_projects_show_right_number(self):
        self.assertEqual(Project.objects.all().count(), 3)

    def test_active_projects_show_right_number(self):
        self.assertEqual(Project.objects.get_active_projects().count(), 1)

    #@tag('temporary')
    def test_draft_projects_dont_show_frontpage(self):
        home_page = self.client.get(reverse_lazy('home'))
        self.assertIn(self.proj2_duplicate.title, str(home_page.content))

    #@tag('temporary')
    def test_approved_projects_show_on_frontpage(self):
        home_page = self.client.get(reverse_lazy('home'))
        self.assertIn(self.public_project.title, str(home_page.content))
        
    def test_root_projects_url_has_correct_status(self):
        project_page = self.client.get(reverse_lazy('all_projects'))
        self.assertEqual(project_page.status_code, 200)

    def test_root_projects_url_shows_active_projects(self):
        project_page = self.client.get(reverse_lazy('all_projects'))
        self.assertIn(self.public_project.title, str(project_page.content))

        draft_project = Project(funding_goal=90000.00, 
            title="This is a draft project", tagline="The best project",
            location="Kathmandu", description="Project description",
            end_date = self.six_months, created_by = self.user,
            project_status = Project.ACTIVE
        )
        draft_project.save()
        self.assertNotIn(draft_project.title, str(project_page.content))

    def test_single_project_renders(self):
        slug = self.public_project_active.slug
        single_project = self.client.get(reverse_lazy('single_project', kwargs={'slug':slug}))
        self.assertEqual(single_project.status_code, 200)
        self.assertIn(self.public_project_active.title, str(single_project.content))
        self.assertIn(self.public_project_active.description, str(single_project.content))

    @tag('temporary')
    def test_only_login_user_can_create_project(self):
        new_project = self.client.get(reverse_lazy('new_project'), follow=True)
        new_redirect = new_project.redirect_chain[0][0]
        self.assertIn("/login", new_redirect)

    def test_logged_in_users_can_create_project(self):
        c = self.client
        c.login(username="test_user", password="usausausa")
        response = c.get(reverse_lazy('new_project'))
        self.assertIn("Create New Project", str(response.content))

    def test_multiple_rewards_can_be_added_to_project(self):
        nine_months = date.today() + relativedelta(months=+9)
        ten_months = date.today() + relativedelta(months=+10)

        reward1 = Reward(name="Reward kind 1", description="Description for reward 1",
                    reward_amout=10000.0, is_digital_product=True, shipping_date=nine_months,
                    project=self.public_project_active)
        reward1.save()
        # 
        reward2 = Reward(name="Reward kind 1", description="Description for reward 1",
                    reward_amout=10000.0, is_digital_product=True, shipping_date=nine_months,
                    project=self.public_project_active)
        reward2.save()

        rewards = self.public_project_active.rewards_for_project
        print(dir(rewards))


        self.assertEqual(rewards.count(), 2)


'''
    name = models.CharField(
                max_length=200,
                blank=False,
                null=True,
                help_text="Write the title for this kind of Reward")
    description = RichTextField(
                blank=False,
                null=True,
                help_text="Write the detail for this kind of Reward")
    reward_amout = models.DecimalField(
        max_digits = 15,
        decimal_places = 2,
        help_text = "How much does the donor have to pay to get this reward?"
    )
    is_digital_product = models.BooleanField(
        default=False,
        help_text="Is it digital product like pdf/ebook that does not need shipping?"
    )
    shipping_date = models.DateField(
        help_text='When will the reward be ready?'
    )
    project = models.ForeignKey(Project, related_name="project_for_reward")

'''



