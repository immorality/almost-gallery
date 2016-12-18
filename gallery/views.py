from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from gallery.models import Album, Photo
from gallery.forms import AlbumForm, PhotoForm, UserForm, UserProfileForm
from django.http import HttpResponse
from django.core.urlresolvers import reverse
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


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()

                registered = True
            else:
                print  user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'gallery/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,
                      user)
                return HttpResponseRedirect(reverse('gallery:index'))

