from django.conf.urls import patterns, url
from django.contrib.auth import authenticate, login

from accounts.views import login_view

urlpatterns = patterns('',
    (r'^login/$', login_view),

)