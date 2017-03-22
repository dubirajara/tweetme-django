from django.test import TestCase

from tweetme.tweets.forms import TweetModelForm


class TweetsFormTest(TestCase):
    def setUp(self):
        self.form = TweetModelForm()

    def test_form_has_fields(self):
        """Tweets_Form must have 1 fields"""
        expected = ('content',)
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_all_required_form_fields(self):
        """Test Tweets_form field is required."""
        form = TweetModelForm({
            'content': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_fields_not_present(self):
        """Tweets_form field is not present."""
        self.assertFalse(self.form.fields.get('user'))
