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
    url(r'^r_eventlist/(?P<Post_id>[0-9]+)/$', views.r_detail, name='r_detail'),
    url(r'^gallery/',include('gallery.urls')),
    url(r'^Cricket/$', views.Cricket, name='Cricket'),
    url(r'^Football/$', views.Football, name='Football'),
    url(r'^Lawn_tennis/$', views.tennis, name='Lawn_tennis'),
    url(r'^Basketball/$', views.BB, name='Basketball'),
    url(r'^Badminton/$', views.Bd, name='Badminton'),
    url(r'^Swimming/$', views.swim, name='Swimming'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
