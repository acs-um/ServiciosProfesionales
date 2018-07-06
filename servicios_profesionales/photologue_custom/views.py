from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import GalleryExtended
from photologue.models import Gallery, Photo
from usuarios.models import MyUser
from servicios.models import Service
from django.urls import reverse
from photologue import forms
from photologue import forms
from django.views.generic.edit import CreateView, UpdateView


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
