from django.db import models

from usuarios.models import MyUser
from Categorias.models import Categoria
from taggit.managers import TaggableManager


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return "{},{}".format(self.name, self.category)
