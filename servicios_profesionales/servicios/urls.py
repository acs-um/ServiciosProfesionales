from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name="all-services"),
    # url(r'^search/$', views.search, name="search-service"),
    url(r'^crear$', login_required(views.CreateService.as_view()), name="createService"),
    url(r'^modificar/(?P<pk>\d+)/$', login_required(views.UpdateService.as_view()), name="updateService"),
    url(r'^borrar/(?P<pk>\d+)/$', login_required(views.DeleteService.as_view()), name="deleteService"),
    url(r'^detalles/(?P<pk>\d+)/$', views.DetailService.as_view(), name="detailService"),
    # path('ingresar', views.signup, name = "SignUp"),
]
