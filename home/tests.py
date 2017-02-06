from django.test import TestCase
from django.test import Client
from django.urls import reverse



class TestHomepage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_works(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(200, resp.status_code)
        self.assertIn("LETS START FUNDING THE NEW NEPAL", str(resp.content))
