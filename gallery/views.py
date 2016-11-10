from django.shortcuts import render, get_object_or_404
from gallery.models import Album, Photo
from django.http import HttpResponse
def index(request):
    context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'gallery/index.html', context=context_dict)

def about(request):
    return HttpResponse("About Page")

def albums(request):
    list_albums = Album.objects.all()
    context_albums = {'albums' : list_albums}

    return render(request, 'gallery/albums.html', context=context_albums)

def photos(request, album_id):
    context_dict = {}
    albums = get_object_or_404(Album, pk=album_id)
    photos = Photo.objects.filter(album=album_id)
    context_dict['photos'] = photos
    context_dict['albums'] = albums
    return render(request, 'gallery/photos.html', context_dict)



