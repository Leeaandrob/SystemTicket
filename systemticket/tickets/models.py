#coding:utf-8

from django.db import models
from systemticket.navios.models import Navio
# Create your models here.

class Ticket(models.Model):
	descricao = models.CharField(max_length=100)
	navio = models.ForeignKey(Navio)
	
	def __unicode__(self):
		return unicode(self.descricao)


class Observacao(models.Model):
	descricao = models.TextField(max_length=100)
	ticket = models.ForeignKey(Ticket,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.descricao)	