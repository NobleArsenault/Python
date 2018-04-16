from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^times$', views.create),
    url(r'^times/timedisplay$', views.create),
    url(r'^$', views.index)     # This line has changed!
  ]
