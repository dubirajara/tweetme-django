from django.test import TestCase
from django.shortcuts import resolve_url as r

from model_mommy import mommy


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


class CreateViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('create'))

    def test_get(self):
        """GET 'create View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'create View' must use template create_view.html and form.html'"""
        self.assertTemplateUsed(self.response, 'tweets/create_view.html')
        self.assertTemplateUsed(self.response, 'tweets/form.html')

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class UpdateViewTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet', pk=2)
        self.response = self.client.get(r('update', self.tweet.id))

    def test_get(self):
        """GET 'update View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'update View' must use template update_view.html and form.html"""
        self.assertTemplateUsed(self.response, 'tweets/update_view.html')
        self.assertTemplateUsed(self.response, 'tweets/form.html')

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

