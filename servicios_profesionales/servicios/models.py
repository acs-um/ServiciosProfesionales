from django.db import models

from taggit.managers import TaggableManager

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField

    tags = TaggableManager()