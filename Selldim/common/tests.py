from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class UrlTest(TestCase):
    def testHomePage(self):
        response = self.client.get(reverse('home page'))

        self.assertEqual(response.status_code, 200)

    def testSearch(self):
        response = self.client.get(reverse('product search'))

        self.assertEqual(response.status_code, 200)

    def testSearchByCategory(self):
        response = self.client.get(reverse('product search by category', args=['vehicles']))

        self.assertEqual(response.status_code, 200)
