from django.test import TestCase
from model_mommy import mommy
from .models import Tweet


class ModelTest(TestCase):
    def test_create(self):
        mommy.make('Tweet')
        self.assertTrue(Tweet.objects.exists())

    def test_str(self):
        tweet = mommy.make('Tweet')
        self.assertEqual(tweet.content, str(tweet))
