from django import forms
from gallery.models import Album, Photo

class AlbumForm(forms.ModelForm):
    name = forms.CharField(max_length=40,
                           help_text="Please, type the album name!")
    date_created = forms.DateTimeField(widget=forms.HiddenInput())
    date_modified = forms.DateTimeField(widget=forms.HiddenInput())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Album
        fields = ('name', )

class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=40,
                            help_text="Please, type the photo title!")
    image = forms.ImageField()
    datetime = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Photo
        fields = ('title', )


