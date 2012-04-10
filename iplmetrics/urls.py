from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from player_db.views import IndexView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iplmetrics.views.home', name='home'),
    # url(r'^iplmetrics/', include('iplmetrics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^player_db/', include('player_db.urls'))
)
