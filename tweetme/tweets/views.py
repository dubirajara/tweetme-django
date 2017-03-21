from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet

from .forms import TweetModelForm


class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


class TweetDetailView(DetailView):
    model = Tweet
    # template_name = "detail_view.html"
    # queryset = Tweet.objects.all()

    # def get_object(self):
    #     id = self.kwargs.get('pk')
    #     return Tweet.objects.get(id=id)


class TweetListView(ListView):
    model = Tweet
    # template_name = "list_view.html"
    # queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["list"] = Tweet.objects.all()
        return context

# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         'obj_detail': obj
#     }
#     return render(request, 'detail_view.html', context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'list_view.html', context)
