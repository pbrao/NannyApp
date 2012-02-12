from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('nannyapp.views',
    # Examples:
    # url(r'^$', 'nanny.views.home', name='home'),
    # url(r'^nanny/', include('nanny.foo.urls')),
    url(r'^weeks/$', 'index'),
    url(r'^weeks/(?P<week_id>\d+)/$', 'detail'),
)
