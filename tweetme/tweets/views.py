from django.urls import reverse_lazy as r
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import TweetModelForm
from .models import Tweet
from .mixins import (FormUserNeededMixin,
                     UserOwnerMixin,
                     DeleteTweetMixin,
                     TweetListViewMixin)


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'


class TweetUpdateView(UserOwnerMixin, UpdateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'


class TweetDeleteView(DeleteTweetMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = r('tweet:list')


class TweetDetailView(DetailView):
    model = Tweet


class TweetListView(TweetListViewMixin, ListView):
    model = Tweet

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["list"] = Tweet.objects.all()
        return context
