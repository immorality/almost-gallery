from __future__ import unicode_literals

from django.db import models

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=20)
    image = models.ImageField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

# Create your models here.
