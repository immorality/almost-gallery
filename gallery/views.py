from django.shortcuts import render, get_object_or_404
from gallery.models import Album, Photo
from gallery.forms import AlbumForm, PhotoForm
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

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return index(request)
        else:
            print form.errors
    form = AlbumForm()
    return render(request, 'gallery/add_album.html', {'form': form})

def add_photo(request, album_name_slug):
    try:
        album = Album.objects.get(slug=album_name_slug)
    except Album.DoesNotExist:
        album = None

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if album:
                photo = form.save(commit=False)
                photo.album = album
                photo.image = form.cleaned_data['image']
                photo.user = request.user
                photo.save()
                return photos(request, album_name_slug)
        else:
            print form.errors
    form = PhotoForm()
    context_dict = {'form': form, 'albums': album}
    return render(request, 'gallery/add_photo.html', context_dict)


