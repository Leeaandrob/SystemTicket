# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('systemticket.tickets.views',
	url(r'^novo/$', 'ticket_create', name='ticket_create'),
	url(r'^lista/$', 'ticket_lista', name='ticket_lista'),
	url(r'^editar/(?P<ticket_id>\d+)/$', 'ticket_edit', name='ticket_edit'),
    url(r'^observacoes/(?P<ticket_id>\d+)/$', 'ticket_observacoes', name='ticket_observacoes'),
)