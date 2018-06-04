from django.db import models

from Categorias.models import Categoria
from taggit.managers import TaggableManager
from usuarios.models import MyUser

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = TaggableManager()
    users = models.ManyToManyField(MyUser)

    def __str__(self):
        return "{},{}".format(self.name, self.category)

    def setUser(self, user):
        self.users = user
        return self.save()
