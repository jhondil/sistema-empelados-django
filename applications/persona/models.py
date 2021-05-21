from django.db import models
from applications.departamento.models import Departamento

# Create your models here.

class habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad' #lo que se demuestra en el admin
        verbose_name_plural = 'habilidades'

    def __str__(self):
        return self.habilidad 



class Empleado (models.Model):
    JOB_CHOICES= (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),

    )
    first_name = models.CharField('Nombres',max_length = 150)
    last_name = models.CharField('Apellidos', max_length = 150)
    full_name = models.CharField('Nombres & Apellidos', max_length = 150, blank=True)
    job = models.CharField('trabajo', max_length = 1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', null=True, blank=True)
   #relacion a muchos a muchos
    habilidades  = models.ManyToManyField(habilidades)
    


    class Meta:
        verbose_name = 'Empleado' #lo que se demuestra en el admin
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.first_name + ' ' + self.last_name 
    

