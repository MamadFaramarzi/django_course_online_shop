from django.test import TestCase
from django.urls import reverse


class PageTestView(TestCase):
    def test_home_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_view_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_about_us_view_url(self):
        response = self.client.get("/aboutus/")
        self.assertEqual(response.status_code, 200)

    def test_about_us_view_by_name(self):
        response = self.client.get(reverse("aboutus"))
        self.assertEqual(response.status_code, 200)
