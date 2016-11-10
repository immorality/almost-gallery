from django.conf.urls import url
from gallery import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^albums/', views.albums, name='albums'),
    url(r'^photos/(?P<album_id>[0-9]+)', views.photos, name='photos')
]