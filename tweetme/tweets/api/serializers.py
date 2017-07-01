from rest_framework import serializers


from tweetme.tweets.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'content')