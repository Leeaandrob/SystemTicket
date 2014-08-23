from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'systemticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'systemticket.core.views.home', name='home'),
    url(r'^navios/',include('systemticket.navios.urls', namespace='navios')),
    url(r'^tickets/',include('systemticket.tickets.urls', namespace='tickets')),
)
