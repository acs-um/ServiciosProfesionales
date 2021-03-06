from django.shortcuts import render
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import  DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import models
from .models import Service
from .form import ServiceForm
from photologue_custom.models import GalleryExtended


def index(request):
    if 'search' in request.GET:
        query = models.Service.objects.filter(
            Q(name=request.GET['search']) | Q(tags__name__in=request.GET['search'])
        ).distinct()
        context = {'service_list': query}
    else:
        context = {'service_list': models.Service.objects.all()}
    return render(request, 'servicios/index.html', context)

class DetailService(DetailView):
    model = Service
    template_name = 'servicios/detailService.html'

    def get_success_url(self):
        return reverse('all-services')


class CreateService(CreateView):
    model = Service
    fields = ['name', 'description', 'category', 'tags']
    form = ServiceForm()
    template_name = "servicios/createService.html"

    def form_valid(self, form):
        service = form.save(commit=False)
        service.user = self.request.user
        service.save()
        GalleryExtended.nuevo(service, self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('all-services')


class UpdateService(UpdateView):
    model = Service
    fields = '__all__'
    form = ServiceForm()
    template_name = "servicios/updateService.html"

    def get_success_url(self):
        return reverse('all-services')


class DeleteService(DeleteView):
    model = Service
    fields = '__all__'
    form = ServiceForm()
    template_name = "servicios/deleteService.html"

    def get_context_data(self, **kwargs):
        context_data = super(DeleteService, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        service = Service.objects.get(id=int(pk))
        context_data.update({'service': service})
        return context_data

    def get_success_url(self):
        return reverse('all-services')
