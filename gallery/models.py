from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='./static/profile_images', blank=True)

    def __unicode__(self):
        return self.username

class Album(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

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
