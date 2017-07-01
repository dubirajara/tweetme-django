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
            self.user, self.email, self.password
        )
        self.tweet = Tweet.objects.create(
            user=user, content='test app'
        )

    def api_signin_and_get(self):
        self.login = self.client.login(
            username=self.user, password=self.password
        )
        self.response = self.client.get(r('tweet-api:list'))
        self.get_json = json.loads(self.response.content.decode('utf-8'))

    def test_api_get(self):
        """GET 'list api' must return status code 200"""
        self.api_signin_and_get()
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    # def test_api_access_forbidden(self):
    #     """GET page not logged in must return status code 403"""
    #     self.response = self.client.get(r('tweet-api:list'))
    #     self.assertEqual(status.HTTP_403_FORBIDDEN, self.response.status_code)
