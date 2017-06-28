from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import resolve_url as r

from tweetme.tweets.models import Tweet

User = get_user_model()


class ModelTest(TestCase):
    def setUp(self):
        self.tweet_user = User.objects.create(username='tweetadmin1234')
        self.tweet = Tweet.objects.create(user=User.objects.first(), content='hello word')

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Tweet.objects.exists())

    def test_tweet_items(self):
        """Check models items"""
        self.assertTrue(self.tweet.user, self.tweet_user)
        self.assertTrue(self.tweet.content, 'hello word')
        self.assertTrue(self.tweet.id, 1)

    def test_instance(self):
        """Check models data instance"""
        self.assertIsInstance(self.tweet, Tweet)

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
