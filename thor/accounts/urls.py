from django.conf.urls.defaults import *

urlpatterns = patterns('',
  # Login / logout
  (r'^login/$', 'django.contrib.auth.views.login'),

  )