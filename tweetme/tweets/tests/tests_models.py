from django.test import TestCase
from django.shortcuts import resolve_url as r

from model_mommy import mommy

from tweetme.tweets.models import Tweet


class ModelTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet')

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Tweet.objects.exists())

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual(self.tweet.content, str(self.tweet))

    def test_ordering(self):
        """Check ordering to show"""
        self.assertListEqual(['-timestamp'], Tweet._meta.ordering)

    def test_get_absolute_url(self):
        """Check get_absolute_url slug idea_details url"""
        url = r('tweet:detail', pk=self.tweet.pk)
        self.assertEqual(url, self.tweet.get_absolute_url())
