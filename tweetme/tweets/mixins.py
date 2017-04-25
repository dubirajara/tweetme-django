from django import forms
from django.db.models import Q
from django.forms.utils import ErrorList
from django.http import Http404

from .models import Tweet


class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to continue'])
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['This user is not allowed to change this data'])
            return self.form_invalid(form)


class DeleteTweetMixin(object):
    def get_object(self):
        obj = super(DeleteTweetMixin, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class TweetListViewMixin(object):
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
