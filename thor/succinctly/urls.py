from django.conf.urls import patterns, url

from succinctly import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)