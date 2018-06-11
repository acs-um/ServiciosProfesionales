from django.db import models
from usuarios.models import MyUser

from photologue.models import Gallery


class GalleryExtended(models.Model):
    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(Gallery, related_name='extended', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.gallery.title
