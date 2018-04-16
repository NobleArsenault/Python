from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/delete$', views.delete),
# can also be written like this url(r'^/edit(?P<number>\d+)$', views.edit),
    url(r'^(?P<number>\d+)/edit$', views.edit),

  ]