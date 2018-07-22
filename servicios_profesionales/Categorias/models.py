from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=45, help_text="Nombre de la Categoria")
    description = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.name
