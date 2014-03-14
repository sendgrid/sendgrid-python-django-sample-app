from django.conf.urls import patterns, url, include
from SGapp.views import index
urlpatterns = patterns('',
    (r'^$', index),
)
