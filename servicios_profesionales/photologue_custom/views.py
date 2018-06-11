from .forms import GalleryExtendedForm
from .models import GalleryExtended
from photologue.models import Gallery
from usuarios.models import MyUser
from servicios.models import Service
from django.urls import reverse
from django.views.generic.edit import CreateView


class CreateExtendedGallery(CreateView):
    model = GalleryExtended
    fields = ['title']
    form = GalleryExtendedForm()
    template_name = "servicios/createService.html"

    def __init__(self, user, service):
        print('Galeria creada')
        usuario = MyUser.objects.get(email=user)
        servicio = Service.objects.get(id=service)
        string = usuario.first_name + '-' + servicio.name
        gallery = Gallery.objects.create(title=string, slug=string)
        GalleryExtended.objects.create(user=usuario, gallery=gallery)
        print('Galeria creada')
        return None

    def get_success_url(self):
        return reverse('all-services')
