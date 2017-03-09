from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy
from .models import Tweet


class ListViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('list'))


    def test_get(self):
        """GET 'list View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'list View' must use template tweet_list.html"""
        self.assertTemplateUsed(self.response, 'tweets/tweet_list.html')


class DetailViewTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet', pk=2)
        self.response = self.client.get(self.tweet.get_absolute_url())


    def test_get(self):
        """GET 'detail View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'detail View' must use template tweet_detail.html"""
        self.assertTemplateUsed(self.response, 'tweets/tweet_detail.html')

    def test_id(self):
        self.assertEqual(2, self.tweet.pk)


class ModelTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet')

    def test_create(self):
        self.assertTrue(Tweet.objects.exists())

    def test_str(self):
        self.assertEqual(self.tweet.content, str(self.tweet))
