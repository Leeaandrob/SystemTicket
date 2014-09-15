#coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from systemticket.tickets.forms import TicketForm,ObservacaoForm
from systemticket.tickets.models import Ticket,Observacao

def ticket_create(request):
	form = TicketForm(request.POST)
	if not form.is_valid():
		return render(request, 'ticket_novo.html',{'form':form})
	obj = form.save()
	return HttpResponseRedirect('/tickets/lista/')

def ticket_lista(request):
	listar_tickets = Ticket.objects.all().order_by('-id')
	return render(request,"ticket_lista.html",{'tickets':listar_tickets})

def ticket_edit(request,ticket_id):
	ticket = get_object_or_404(Ticket,id=ticket_id)
	if request.method == 'POST':
		return edit_post(request,ticket)
	else:
		return render(request,"ticket_editar.html",{'form':TicketForm(instance=ticket),'ticket':ticket})


def ticket_post(request):
	form = TicketForm(request.POST)
	if not form.is_valid():
		return render(request, 'ticket_novo.html',{'form': form})
	obj = form.save()
	return HttpResponseRedirect("/tickets/lista/")

def ticket_get(request):
	form = TicketForm()
	return render(request,"ticket_novo.html",{'form':form})


def edit_post(request,ticket):
	form = TicketForm(request.POST,instance=ticket)
	if not form.is_valid():
		return render(request, 'ticket_editar.html',{'form': form,'ticket':ticket})

	obj = form.save(commit=False)
	obj.save()
	return HttpResponseRedirect("/tickets/lista/")

def ticket_observacoes(request,ticket_id):
	ticket = get_object_or_404(Ticket,id=ticket_id)
	if request.method == 'POST':
		form = ObservacaoForm(request.POST)
		if not form.is_valid():
			return render(request, 'ticket_observacoes.html', {'form': form,'ticket':ticket,'obs':Observacao.objects.filter(ticket=ticket)})
		obj = form.save()
		obj.ticket = ticket
		obj.save()
	form = ObservacaoForm()
	return render(request, 'ticket_observacoes.html', {'form': form,'ticket':ticket,'obs':Observacao.objects.filter(ticket=ticket)})
	
    
