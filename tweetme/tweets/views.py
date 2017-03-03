from django.shortcuts import render


def tweet_detail_view(request, id=1):
    return render(request, 'detail_view.html', {})


def tweet_list_view(request):
    return render(request, 'list_view.html', {})
