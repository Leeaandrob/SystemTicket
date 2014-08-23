#coding: utf-8
from django.db import models
# Create your models here.

class Navio(models.Model):
    nome = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    designacao_hughes = models.CharField(max_length=100)
    designacao_skyreach = models.CharField(max_length=100)
    esn_modem=models.CharField(max_length=100)
    solucao_instalada=models.CharField(max_length=100)
   
    def __unicode__(self):
        return unicode(self.nome)