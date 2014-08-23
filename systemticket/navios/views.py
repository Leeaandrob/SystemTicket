#coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from systemticket.navios.forms import NavioForm
from systemticket.navios.models import Navio

def navio_create(request):
	form = NavioForm(request.POST)
	if not form.is_valid():
		return render(request, 'navio_novo.html',{'form': form})
	obj = form.save()
	return HttpResponseRedirect("/navios/lista/")

def navio_lista(request):
	return render(request, 'navio_lista.html', {'navios': Navio.objects.all()})


def navio_edit(request,navio_id):

    navio = get_object_or_404(Navio,id=navio_id)
    if request.method == 'POST':
        return edit_navio(request,navio)
    else:
        return request_navio(request,navio)

def edit_navio(request,navio):
    '''
        @edit_funcao: View para alterar os dados de um funcao
    '''
    form = NavioForm(request.POST,instance=navio)
    if form.is_valid():
        navio = form.save(commit=False)
        navio.save()
        return HttpResponseRedirect('/navios/lista')
    else:
        return render(request,'navio_editar.html',{'form':form})

def request_navio(request,navio):
    '''
        @request_funcao: View para obter os dados de um determinado funcao
    '''
    form = NavioForm(instance=navio)
    return render(request, 'navio_editar.html', {'form': form})