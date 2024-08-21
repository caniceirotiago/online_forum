from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from forum.models import Forum, Post, Topic

class ForumAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.forum = Forum.objects.create(name="Test Forum", description="Test Description")

    def test_forum_list(self):
        response = self.client.get(reverse('forum-list'))  # 'forum-list' should be the name of the URL for the ForumAPI list view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_forum_retrieve(self):
        response = self.client.get(reverse('forum-detail', kwargs={'pk': self.forum.id}))  # 'forum-detail' should be the name of the URL for the ForumAPI detail view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.forum.name)

class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.forum = Forum.objects.create(name="Test Forum", description="Test Description")
        self.post = Post.objects.create(forum=self.forum, title="Test Post", content="Test Content", created_by=self.user)

    def test_post_list(self):
        response = self.client.get(reverse('post-list'))  # 'post-list' should be the name of the URL for the PostAPI list view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_retrieve(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.id}))  # 'post-detail' should be the name of the URL for the PostAPI detail view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

class TopicAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.forum = Forum.objects.create(name="Test Forum", description="Test Description")
        self.topic = Topic.objects.create(forum=self.forum, title="Test Topic", content="Test Content", created_by=self.user)

    def test_topic_list(self):
        response = self.client.get(reverse('topic-list'))  # 'topic-list' should be the name of the URL for the TopicAPI list view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_topic_list_filter_by_forum(self):
        response = self.client.get(reverse('topic-list'), {'forum_id': self.forum.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_topic_list_filter_by_user(self):
        response = self.client.get(reverse('topic-list'), {'user_id': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_topic_retrieve(self):
        response = self.client.get(reverse('topic-detail', kwargs={'pk': self.topic.id}))  # 'topic-detail' should be the name of the URL for the TopicAPI detail view
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.topic.title)