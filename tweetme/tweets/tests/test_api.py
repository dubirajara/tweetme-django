import json

from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from tweetme.tweets.models import Tweet


class TweetListApiViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'

        user = User.objects.create_user(
            self.user, self.email, self.password,
            first_name='Diego', last_name='Test',
        )
        self.tweet = Tweet.objects.create(
            user=user, content='test app',
        )

        self.response = self.client.get(r('tweet-api:list'))
        self.get_json = json.loads(self.response.content.decode('utf-8'))

    def test_api_get(self):
        """GET 'list api' must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_api_contents(self):
        """Test request must contain and return json contents"""
        self.assertEqual(self.get_json, [{'content': 'test app',
                                          'user': {'email': 'test@djangoapp.com',
                                                   'first_name': 'Diego',
                                                   'follower_count': 0,
                                                   'last_name': 'Test',
                                                   'username': 'diego'}}])
