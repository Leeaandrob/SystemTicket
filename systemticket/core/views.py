#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse as r


def home(request):
	return render(request, 'base.html')