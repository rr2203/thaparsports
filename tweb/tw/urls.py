from django.conf.urls import url,include
from . import views
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^eventlist/$', views.eventlist, name='eventlist'),
    url(r'^r_eventlist/$', views.r_eventlist, name='r_eventlist'),
    url(r'^Our_achievements/$', views.achieve, name='Our_achievements'),
    url(r'^eventlist/(?P<Post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^gallery/',include('gallery.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
