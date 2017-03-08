from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


class TweetDetailView(DetailView):
    model = Tweet
    # template_name = "detail_view.html"
    # queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=2)


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
