from datetime import date
from dateutil.relativedelta import relativedelta

import django
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, reverse_lazy
from django.test import tag

from .models import Project


class ProjectHomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.proj1 = Project(funding_goal=90000.00, 
            title="Test title 1", tagline="The best project",
            location="Kathmandu", description="Project description",
            )
        
        six_months = date.today() + relativedelta(months=+6)
        user = User(username="test_user")
        user.save()
        
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
        
    def test_root_url_shows_all_projects(self):
        project_page = self.client.get(reverse_lazy('all_projects'))
        self.assertEqual(project_page.status_code, 200)



