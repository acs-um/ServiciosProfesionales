from django.shortcuts import render
from django.db.models import Q
from . import models


def index(request):
    if 'search' in request.GET:
        query = models.Service.objects.filter(
            Q(name=request.GET['search']) | Q(tags__name__in=request.GET['search'])
        ).distinct()
        context = {'service_list': query}
    else:
        context = {'service_list': models.Service.objects.all()}
    return render(request, 'servicios/index.html', context)
