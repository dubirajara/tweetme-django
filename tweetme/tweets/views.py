from django.shortcuts import render
from .models import Tweet


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        'obj_detail': obj
    }
    return render(request, 'detail_view.html', context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        'obj_list': queryset
    }
    return render(request, 'list_view.html', context)
