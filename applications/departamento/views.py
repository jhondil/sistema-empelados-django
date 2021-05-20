from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


from applications.persona.models import *
from applications.departamento.models import *

from .form import NewDepartamentoForm
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/list.html"
    context_object_name='departamentos'


class NewDepartamentoView(FormView):
    """NewDepartamentoView definition."""

    template_name = 'departamento/new-departamento.html'
    form_class= NewDepartamentoForm
    success_url= '/'

    def form_valid(self, form):

        #crear una instancia dle modelo departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name= form.cleaned_data['shortname']
        )
        #guardar en la base de datos
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']


        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )

        

        return super(NewDepartamentoView,self).form_valid(form)