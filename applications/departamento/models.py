from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length = 150, )
    shor_name = models.CharField('Nombre Corto', max_length = 50, unique=True)
    anulate = models.BooleanField('Anulado', default=False,)

    def __str__(self):
        return str(self.id) + '-' + self.shor_name
    

    class Meta:
        verbose_name = 'Departamento' #lo que se demuestra en el admin
        verbose_name_plural = 'Departamentos'
        ordering=['-name']
        unique_together=('name','shor_name') #que no se reguistre una combinacion igual 
    