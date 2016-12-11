from django.conf.urls import url, patterns
from django.contrib import admin
from gallery import views
from django.conf.urls import include
from almostGallery import settings




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
]