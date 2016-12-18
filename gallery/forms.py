from django import forms
from gallery.models import Album, Photo, User, UserProfile


class AlbumForm(forms.ModelForm):
    name = forms.CharField(max_length=40,
                           help_text="Please, type the album name!")
    date_created = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    date_modified = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Album
        fields = ('name', )

class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=40,
                            help_text="Please, type the photo title!")
    image = forms.ImageField()
    datetime = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Photo
        fields = ('title', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


