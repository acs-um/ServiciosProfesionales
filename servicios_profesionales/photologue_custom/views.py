from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from photologue.models import Gallery
from photologue import forms


class CreateExtendedGallery(CreateView):
    model = Gallery
    fields = ['photos']

    def get_success_url(self):
        return reverse('all-galleries')


class UpdateGalleryExtended(UpdateView):
    model = Gallery
    fields = ['description', 'photos']
    form = forms.Gallery
    template_name = "gallery_extended/updateGallery.html"

    def get_success_url(self):
        return reverse('personDetails')
