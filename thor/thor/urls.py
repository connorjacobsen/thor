from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^succinctly/', include('succinctly.urls', namespace='succinctly')),
    url(r'^$', 'succinctly.views.home'),

    # user auth urls
    url(r'^accounts/login/$', 'accounts.views.login'),
    url(r'^accounts/auth/$', 'accounts.views.auth_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout'),
    url(r'^accounts/loggedin/$', 'accounts.views.loggedin'),
    url(r'^accounts/invalid/$', 'accounts.views.invalid_login'),

    # user registration urls
    url(r'^accounts/register/$', 'accounts.views.register_user'),
    url(r'^accounts/register_success/$', 'accounts.views.register_success'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
