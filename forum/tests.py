from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from forum.models import Forum, Post, Topic

class ForumAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # POSITIVE test case - create a forum
    def test_forum_create(self):
        self.forum_data = {'name': 'Test Forum', 'description': 'Test Description'}
        response = self.client.post(reverse('forums-list'), self.forum_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test Forum')
        self.assertEqual(response.data['description'], 'Test Description')
        self.assertIn('id', response.data)
        self.assertIsInstance(response.data['id'], int)


    # NEGATIVE test case - create a forum (no name)
    def test_forum_create_bad_request(self):
        self.forum_data = {'description': 'Test Description'}
        response = self.client.post(reverse('forums-list'), self.forum_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # NEGATIVE test case - create a forum (more than 100 characters on name)
    def test_forum_create_bad_request_length(self):
        string_with_100_char = "xTest ForumTest ForumTest ForumTest ForumTest ForumTest ForumTest ForumTest ForumTest ForumTest Forum"
        self.forum_data = {'name': string_with_100_char, 'description': 'Test Description'}
        response = self.client.post(reverse('forums-list'), self.forum_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg="Expected a 400 Bad Request when name is too long")

    # NEGATIVE test case - create a forum (empty name)
    def test_forum_create_bad_request_empty_name(self):
        self.forum_data = {'name': '', 'description': 'Test Description'}
        response = self.client.post(reverse('forums-list'), self.forum_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg="Expected a 400 Bad Request when name is missing")
