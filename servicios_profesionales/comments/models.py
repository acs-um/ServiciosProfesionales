from django.db import models
from usuarios.models import MyUser
from servicios.models import Service

# Create your models here.

class Comment(models.Model):
    description = models.TextField()
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE) 
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
       
    class Meta:
        ordering = ('created_at',)

    def __str__ (self):
        return "{},{},{}".format(self.description, self.created_by, self.update_at)