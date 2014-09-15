# -*- coding: utf-8 -*-

from django.db import models
from systemticket.navios.models import Navio
# Create your models here.

STATUS = (
	('open', 'aberto'),
	('closed', 'fechado'),
	('obs', 'observacao')
	)

class Ticket(models.Model):
	sumario = models.CharField(max_length=100)
	descricao = models.CharField(max_length=100)
	numero_chamado = models.CharField(max_length=7)
	navio = models.ForeignKey(Navio)
	status = models.CharField(max_length=100, choices=STATUS, default='open')
	solucao = models.CharField(max_length=100)
	
	def __unicode__(self):
		return unicode(self.descricao)


class Observacao(models.Model):
	descricao = models.CharField(max_length=100)
	ticket = models.ForeignKey(Ticket,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.descricao)	