from django.db import models

# Create your models here
class Categoria(models.Model):
    name=models.CharField(max_length=20, help_text="Nombre de la Categoria")
    



