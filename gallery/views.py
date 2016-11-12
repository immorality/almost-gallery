from django.shortcuts import render, get_object_or_404
from gallery.models import Album, Photo
from django.http import HttpResponse
def index(request):
    context_dict = {}
    albums = Album.objects.all()
    context_dict['albums'] = albums
    return render(request, 'gallery/index.html', context=context_dict)

def about(request):
    return HttpResponse("About Page")

def albums(request):
    list_albums = Album.objects.all()
    context_albums = {'albums' : list_albums}

    return render(request, 'gallery/albums.html', context=context_albums)

def photos(request, album_name_slug):
    context_dict = {}
    try:
        albums = get_object_or_404(Album, slug= album_name_slug)
        photos = Photo.objects.filter(album=albums)
        context_dict['photos'] = photos
        context_dict['albums'] = albums
    except Album.DoesNotExist:
        context_dict['albums'] = None
        context_dict['photos'] = None

    return render(request, 'gallery/photos.html', context_dict)



