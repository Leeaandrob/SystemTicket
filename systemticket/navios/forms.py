# coding: utf-8

from django import forms
from systemticket.navios.models import Navio
from django.core.exceptions import ValidationError

from django.contrib import admin


class NavioForm(forms.ModelForm):
    class Meta:
        model = Navio

