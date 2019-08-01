from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url('index',views.index,name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.details,name='details'),
    url(r'^(?P<pk>[0-9]+)/results/$',views.results,name='results'),
    url(r'^(?P<pk>[0-9]+)/vote/$',views.vote,name='vote'),
]
