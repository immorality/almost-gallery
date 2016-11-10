from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='./static/images')
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

# Create your models here.
