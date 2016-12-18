from django.conf.urls import url, patterns
from gallery import views

app_name='gallery'



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_album/$', views.add_album, name='add_album'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/add_photo/$', views.add_photo, name='add_photo'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/$', views.photos, name='album'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.login, name='login'),
]