from django import template
from gallery.models import Album, Photo

register = template.Library()

@register.inclusion_tag('gallery/albs.html')
def get_album_list(alb=None):
    return {'albs': Album.objects.all(), 'act_albs': alb}

@register.inclusion_tag('gallery/phts.html')
def get_photo_list():
    return {'phts': Photo.objects.all()}

