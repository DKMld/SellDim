from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class UrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='test123123', email='miti_test@abv.bg', password='08120101m')
        self.client.login(username='test123123', password='08120101m')

    def testUserLogin(self):
        response = self.client.login(username='test123123', password='08120101m')
        self.assertEqual(response, True)

    def testUserRegister(self):
        response = self.client.post('register', {'username': 'test123123',
                                                 'email': 'miti_test@abv.bg',
                                                 'password1': '08120101m',
                                                 'password2': '08120101m',
                                                 })
        self.assertEqual(response.status_code, 200)

    def testFavouriteAds(self):
        response = self.client.post(reverse('user favourite ads', args=['test123123']), follow=True)
        self.assertEqual(response.status_code, 200)

    def testUserAds(self):
        response = self.client.post(reverse('user ads', args=['test123123']), follow=True)
        self.assertEqual(response.status_code, 200)

    def testUserProfileDetails(self):
        response = self.client.post(reverse('profile details', args=['test123123']), follow=True)
        self.assertEqual(response.status_code, 200)
