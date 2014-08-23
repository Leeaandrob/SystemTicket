# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('systemticket.navios.views',
	url(r'^novo/$', 'navio_create', name='navio_create'),
	url(r'^lista/$', 'navio_lista', name='navio_lista'),
	url(r'^editar/(?P<navio_id>\d+)/$', 'navio_edit', name='navio_edit'),
)