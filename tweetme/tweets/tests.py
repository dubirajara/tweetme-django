from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy
from .models import Tweet


class ListViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('list_view'))

    def test_get(self):
        """GET 'list View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'list View' must use template list_view.html"""
        self.assertTemplateUsed(self.response, 'list_view.html')


class DetailViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('detail_view'))

    def test_get(self):
        """GET 'detail View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'detail View' must use template detail_view.html"""
        self.assertTemplateUsed(self.response, 'detail_view.html')


class ModelTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet')

    def test_create(self):
        self.assertTrue(Tweet.objects.exists())

    def test_str(self):
        self.assertEqual(self.tweet.content, str(self.tweet))
