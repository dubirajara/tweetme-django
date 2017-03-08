from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


class TweetDetailView(DetailView):
    template_name = 'detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    template_name = 'list_view.html'
    queryset = Tweet.objects.all()


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
