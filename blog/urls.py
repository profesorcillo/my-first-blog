from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^$', views.post_list),
]
