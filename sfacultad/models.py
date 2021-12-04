from django.db import models
from django.db.models.base import Model

# Create your models here.


class comments (models.Model):
    matricula = models.CharField(max_length=9, blank=False, help_text=" Tu matricula")
    aula = models.CharField(max_length=10, blank=False, help_text="Aula")
    num = models.CharField(max_length=15, blank=False,help_text="Numero de computadora utilizado" )
    comment = models.TextField(max_length=500, blank=False, help_text="Escribe tu comentario")
    ip_disp = models.CharField(max_length=64, blank=False, help_text="Escribe la Ip del dispositivo utilizado")
    def __str__(self):
        return '%s (%s - %s - %s)' % (self.matricula, self.aula, self.num, self.ip_disp)