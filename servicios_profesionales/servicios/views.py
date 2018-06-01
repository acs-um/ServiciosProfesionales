from django.shortcuts import render
from .models import Service


def index(request):
    service_list = Service.objects.all()
    context = {'service_list': service_list}
    return render(request, 'servicios/index.html', context)
