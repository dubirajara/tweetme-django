from django.test import TestCase

from model_mommy import mommy

from tweetme.tweets.models import Tweet


class ModelTest(TestCase):
    def setUp(self):
        self.tweet = mommy.make('Tweet')

    def test_create(self):
        self.assertTrue(Tweet.objects.exists())

    def test_str(self):
        self.assertEqual(self.tweet.content, str(self.tweet))