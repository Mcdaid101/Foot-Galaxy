from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1 class='text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl'>The Football Training site you've been looking for</h1>")
        self.assertNotContains(response, "not on the page")
