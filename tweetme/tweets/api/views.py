from rest_framework.generics import ListAPIView

from tweetme.tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListApiView(ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()