from django.shortcuts import render
from django.db.models import Q
from . import models
from .models import Service
from .form import ServiceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse


def index(request):
    if 'search' in request.GET:
        query = models.Service.objects.filter(
            Q(name=request.GET['search']) | Q(tags__name__in=request.GET['search'])
        ).distinct()
        context = {'service_list': query}
    else:
        context = {'service_list': models.Service.objects.all()}
    return render(request, 'servicios/index.html', context)

class CreateService(CreateView):
    model = Service
    fields = '__all__'
    form = ServiceForm()
    template_name = "servicios/createService.html"

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
        service =  Service.objects.get(id=int(pk))
        context_data.update({'service':service})
        return context_data

    def get_success_url(self):
        return reverse('all-services')
