from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contenido(models.Model):
    recurso = models.CharField(max_length=32)
    contenido = models.TextField()
class Css(models.Model):
    recurso = models.CharField(max_length=32)
    css = models.TextField()
