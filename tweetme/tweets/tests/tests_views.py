from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from tweetme.tweets.forms import TweetModelForm


class ListViewTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet', pk=2)
        self.response = self.client.get(r('tweet:list'))

    def test_get(self):
        """GET 'list View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'list View' must use template tweet_list/form/search form and base.html """
        self.assertTemplateUsed(self.response, 'tweets/tweet_list.html')
        self.assertTemplateUsed(self.response, 'tweets/form.html')
        self.assertTemplateUsed(self.response, 'tweets/search_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_html_contains(self):
        self.assertContains(self.response, self.tweet.content)
        self.assertContains(self.response, self.tweet.user)


class DetailViewTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet', pk=2)
        self.response = self.client.get(self.tweet.get_absolute_url())

    def test_get(self):
        """GET 'detail View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'detail View' must use template base/search_form and tweet_detail.html"""
        self.assertTemplateUsed(self.response, 'tweets/tweet_detail.html')
        self.assertTemplateUsed(self.response, 'tweets/search_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_id(self):
        self.assertEqual(2, self.tweet.pk)

    def test_html_contains(self):
        self.assertContains(self.response, self.tweet.content)
        self.assertContains(self.response, self.tweet.user)


class CreateViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('tweet:create'))

    def test_get(self):
        """GET 'create View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'create View' must use template create_view/form/search_form and base.html'"""
        self.assertTemplateUsed(self.response, 'tweets/create_view.html')
        self.assertTemplateUsed(self.response, 'tweets/form.html')
        self.assertTemplateUsed(self.response, 'tweets/search_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_get_create_form(self):
        """GET 'tweet form' must contain form context"""
        self.failUnless(isinstance(
            self.response.context['form'],
            TweetModelForm))


class UpdateViewTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet', pk=2)
        self.response = self.client.get(r('tweet:update', self.tweet.id))

    def test_get(self):
        """GET 'update View' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """'update View' must use template update_view/search_form/form and base.html"""
        self.assertTemplateUsed(self.response, 'tweets/update_view.html')
        self.assertTemplateUsed(self.response, 'tweets/form.html')
        self.assertTemplateUsed(self.response, 'tweets/search_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_get_update_form(self):
        """GET 'update form' must contain form context in html"""
        self.failUnless(isinstance(
            self.response.context['form'],
            TweetModelForm))

    def test_html_contains(self):
        self.assertContains(self.response, self.tweet.content)
