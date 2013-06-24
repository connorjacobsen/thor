from django.conf.urls import patterns, url

from succinctly import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'(?P<article_id>\d+)/$', views.detail, name='detail'),
)