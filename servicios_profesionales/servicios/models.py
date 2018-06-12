from django.db import models
from Categorias.models import Categoria
from usuarios.models import MyUser
from taggit.managers import TaggableManager


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return "{},{}".format(self.name, self.category)
