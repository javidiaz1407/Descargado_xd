# Create your views here.
# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from .models import Laboratorio
from .forms import ClienteForm
from braces.views import LoginRequiredMixin,GroupRequiredMixin

class ListaLaboratorio(LoginRequiredMixin,GroupRequiredMixin, ListView):
	context_object_name = 'laboratorios'
	model = Laboratorio
	template_name = 'laboratorios/lista_laboratorio.html'
	paginate_by = 6
	group_required = ['trabajadores']


	def get_queryset(self):
		queryset = super(ListaLaboratorio, self).get_queryset()
		# búsqueda
		q = self.request.GET.get('q', '')
		if q:
			queryset = queryset.filter(
				Q(nombre__icontains=q) |
				Q(codigo__icontains=q)
				)
		return queryset


# Create your views here.
class DetalleView(LoginRequiredMixin, DetailView):
	model = Laboratorio
	template_name = 'laboratorios/detalle_laboratorio.html'


class ActualizarView(UpdateView):
	form_class = ClienteForm
	template_name = 'laboratorios/editar_laboratorios.html'
	model = Laboratorio
	success_url='/lista_laboratorio'



class EliminarView(GroupRequiredMixin, DeleteView):
	model = Laboratorio
	success_url='/lista_laboratorio'
	template_name = 'laboratorios/eliminar_laboratorio.html'
	group_required = ['administrador']



class CreateLaboratorio(LoginRequiredMixin, CreateView):
	
	template_name = 'laboratorios/crear_laboratorios.html'
	model = Laboratorio
	success_url = '/lista_laboratorio'