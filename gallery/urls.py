from django.conf.urls import url
from gallery import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    #url(r'^album/(?P<album_id>[0-9]+)', views.photos, name='album'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/$', views.photos, name='album'),
]