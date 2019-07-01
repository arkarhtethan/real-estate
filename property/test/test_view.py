from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestPropertyHomeView(TestCase):

    def setUp(self):

        self.url = reverse("property:home")

        self.client = Client()

    def test_page_status(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)