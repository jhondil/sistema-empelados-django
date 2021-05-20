from django.contrib import admin
from django.urls import path
from . import views

app_name= "persona_app"
urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shorname>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('agregar-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccesView.as_view(), name='correcto'),
    path('modificar/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('eliminar/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar'),
]
