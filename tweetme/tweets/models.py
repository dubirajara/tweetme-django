from django.conf import settings
from django.db import models
from django.urls import reverse as r
from .validators import validate_content


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return r('tweet:detail', kwargs={'pk':self.pk})
