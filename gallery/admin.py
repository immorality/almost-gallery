from django.contrib import admin
from gallery.models import Album, Photo
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)