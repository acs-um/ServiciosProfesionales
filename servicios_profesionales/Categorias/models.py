from django.db import models

# Create your models here
class categoria(models.Model):
    name=models.CharField(max_length=200, help_text="Nombre de la clase")


