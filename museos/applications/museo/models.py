from django.db import models


class Pais(models.Model):
    """ representa el pais al que pertenece un museo """
    nombre = models.CharField(
      'Nombre Pais',
      max_length=50
    )


    class Meta:
      verbose_name = 'Pais'
      verbose_name_plural = 'Paises'
    
    def __str__(self):
      return self.nombre


class Museo(models.Model):
    """ representa un museo"""
    nombre = models.CharField(
      'Nombre Museo',
      max_length=80
    )
    pais = models.ForeignKey(
      'Pais', 
      on_delete=models.CASCADE
    )


    class Meta:
      verbose_name = 'Museo'
      verbose_name_plural = 'Museos'
    
    def __str__(self):
      return self.nombre