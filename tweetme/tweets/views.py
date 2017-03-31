from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin


class TweetCreateView(FormUserNeededMixin, CreateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/'


class TweetDetailView(DetailView):
    model = Tweet


class TweetListView(ListView):
    model = Tweet

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["list"] = Tweet.objects.all()
        return context
