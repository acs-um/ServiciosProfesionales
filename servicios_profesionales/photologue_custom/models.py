from django.db import models
from usuarios.models import MyUser
from servicios.models import Service
from photologue.models import Gallery


class GalleryExtended(models.Model):
    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(Gallery, related_name='extended', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.gallery.title

    @staticmethod
    def nuevo(service, user):
        string = user.first_name + '-' + service.name
        gallery = Gallery.objects.create(title=string, slug=string)
        return (GalleryExtended.objects.create(gallery=gallery, user=user, service=service))
