from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='test123123', email='miti_test@abv.bg', password='08120101m')
        self.client.login(username='test123123', password='08120101m')

    def testChatRoomPage(self):
        response = self.client.get(reverse('chat room'), follow=True)
        self.assertEqual(response.status_code, 200)