from django.contrib import admin
from gallery.models import Album, Photo, UserProfile
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
admin.site.register(UserProfile)