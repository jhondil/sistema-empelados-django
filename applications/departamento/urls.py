from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='crear-departamento'
        ),
    path(
        'listar-departamento/', 
        views.DepartamentoListView.as_view(), 
        name='listar-departamento'
        ),
    
]
