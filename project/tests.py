from datetime import date
from dateutil.relativedelta import relativedelta

import django
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Project


class ProjectTest(TestCase):
    def setUp(self):
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

    def test_cannot_save_without_user(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            self.proj1.save()

    def test_saves_project_with_no_error(self):
        self.assertEqual(self.proj2.project_status, Project.DRAFTED)

    def test_slug_not_empty(self):
        self.assertEqual(self.proj2.slug, "test-title-1")

    def test_slugs_are_unique(self):
        self.assertNotEqual(self.proj2.slug, self.proj2_duplicate.slug)


