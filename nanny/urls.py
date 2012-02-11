from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nanny.views.home', name='home'),
    # url(r'^nanny/', include('nanny.foo.urls')),
    url(r'^nannyapp/weeks/$', 'nannyapp.views.index'),
    url(r'^nannyapp/weeks/(?P<week_id>\d+)/$', 'nannyapp.views.detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
