from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .models import Empleado


# Create your views here.
################################################
############ List View #########################
################################################
# listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list-all.html'
    model = Empleado

# listar todos los empleados  que pertenecen a un area de la empresa


class ListByAreaEmpleado(ListView):
    """Lista empleados de un area

    Args:
        ListView ([type]): [description]
    """

    template_name = 'persona/list-by-area.html'
    # queryset= Empleado.objects.filter(

    #     departamento__shor_name = 'otro'
    # )

    def get_queryset(self):
        # recoger variables desde url
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


# listar todos los empleados por palabra clave
class ListEmpleadoByKword(ListView):
    """listar todos los empleados por palabra clave por un buscador html
    """

    template_name = 'persona/list-by-kword.html'
    context_object_name = 'empleados'  # esto es el resultado para pintar en el html

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# Listar habilidades de un empleado ManyToMany


class ListHabilidadesEmpleado(ListView):
    model = Empleado
    context_object_name = 'habilidades'
    template_name = 'persona/habilidades.html'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=6)
        return empleado.habilidades.all


################################################
############ Details View #########################
################################################

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail-empleado.html'


################################################
############ Create View #######################
################################################


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # fields = ('__all__') #traer los datos
    fields = [
            'first_name', 
            'last_name', 
            'job', 
            'departamento',
            'habilidades',
            ]  
    # success_url='.' #recarga la misma pagina
    # recarga la misma pagina
    success_url = reverse_lazy('persona_app:correcto')

    #si los datos del formulario son validos entra a la siguiente función
    def form_valid(self, form):
        #se recupera todos los datos del formulario
        # empleado=form.save() #para que lo guarde en la base de datos
        empleado=form.save(commit=False) #para solo hacer solo la isntancia y no guardar en al base de datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class SuccesView(TemplateView):
    template_name = "persona/success.html"

################################################
############ Update View #######################
################################################


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
            'first_name', 
            'last_name', 
            'job', 
            'departamento',
            'habilidades',
            ] 
    success_url = reverse_lazy('persona_app:correcto')

    #ecuperar datos desde el formulario por post
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


################################################
############ Delete View #######################
################################################


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')

