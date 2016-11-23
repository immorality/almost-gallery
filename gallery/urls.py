from django.conf.urls import url
from gallery import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_album/$', views.add_album, name='add_album'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/add_photo/$', views.add_photo, name='add_photo'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/$', views.photos, name='album'),
]