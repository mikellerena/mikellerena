from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import EquipoForm, EmpleadoForm, ProcesoForm
from .models import Equipo, Empleado, Proceso

# Create your views here.

"""Vista para el formulario de creacion de equipo"""
class CreateEquipoView(View):
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de empleados'
        }
        return render(request, 'create_equipo_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo_list')

        return render(request, 'create_equipo_form.html', {'form': form})


"""Vista para ver el listado de equipos"""
class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipo_list.html'
    queryset = Equipo.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(EquipoListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Equipos existentes'
        return context


"""Vista para ver el detalle de los equipos"""
class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los equipos'
        return context

"""Vista para modificar los datos de los equipos"""
class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo_update.html'
    success_url = reverse_lazy('equipo_list')

    def get_context_data(self, **kwargs):
        context = super(EquipoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar equipos'
        return context

"""Vista para el formulario de creacion de empleado"""
class CreateEmpleadoView(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de empleados'
        }
        return render(request, 'create_empleado_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')

        return render(request, 'create_empleado_form.html', {'form': form})


"""Vista para ver el listado de empleado"""
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    queryset = Empleado.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Empleados existentes'
        return context


"""Vista para ver el detalle de los empleados"""
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los empleados'
        return context

"""Vista para modificar los datos de los empleados"""
class EmpleadoUpdateView(UpdateView):
    model = Empleado
<<<<<<< Updated upstream
    form_class = EmpleadoForm
=======

>>>>>>> Stashed changes
    template_name = 'empleado_update.html'
    success_url = reverse_lazy('empleado_list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar empleados'
        return context
"""Vista para el formulario de creación de procesos"""
class CreateProcesoView(View):
    def get(self, request, *args, **kwargs):
        form = ProcesoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de procesos'
        }
        return render(request, 'create_proceso_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proceso_list')

        return render(request, 'create_proceso_form.html', {'form': form})


"""Vista para ver el listado de procesos"""
class ProcesoListView(ListView):
    model = Proceso
    template_name = 'proceso_list.html'
    queryset = Proceso.objects.order_by('codigo_proceso')

    def get_context_data(self, **kwargs):
        context = super(ProcesoListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Procesos existentes'
        return context


"""Vista para ver el detalle de los procesos"""
class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los procesos'
        return context

"""Vista para modificar los datos de los procesos"""
class ProcesoUpdateView(UpdateView):
    model = Proceso
    form_class = Proceso
    template_name = 'proceso_update.html'
    success_url = reverse_lazy('proceso_list')

    def get_context_data(self, **kwargs):
        context = super(ProcesoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar procesos'
        return context
