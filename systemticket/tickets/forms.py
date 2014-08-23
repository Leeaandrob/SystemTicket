# coding: utf-8

from django import forms
from systemticket.tickets.models import Ticket,Observacao
from django.core.exceptions import ValidationError

from django.contrib import admin


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket

class ObservacaoForm(forms.ModelForm):
    class Meta:
        model = Observacao