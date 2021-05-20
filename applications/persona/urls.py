from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"
urlpatterns = [
    path('',
         views.InicioView.as_view(),
         name="inicio-persona"
         ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleado-all'
    ),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado-detail'
    ),
    path(
        'listar-by-area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name="listar-area"
    ),
    path(
        'listar-empleados-admin/',
        views.ListAllEmpleadosAdmin.as_view(),
        name="listar-empleados-admin"
    ),
    path(
        'modificar/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar'),
    path(
        'eliminar/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar'),
    path(
        'agregar-empleado/',
        views.EmpleadoCreateView.as_view(),
        name="agregar-empleado"
    ),
    ##################################################################



    path(
        'buscar-empleado/',
        views.ListEmpleadoByKword.as_view(),

    ),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),


    path('success/', views.SuccesView.as_view(), name='correcto'),


]
