from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name="all-services"),
    # url(r'^search/$', views.search, name="search-service"),
    url(r'^crear$', login_required(views.CreateService.as_view()), name="createService"),
    url(r'^modificar/(?P<pk>\d+)/$', views.UpdateService.as_view(), name="updateService"),
    url(r'^borrar/(?P<pk>\d+)/$', views.DeleteService.as_view(), name="deleteService"),
    # path('ingresar', views.signup, name = "SignUp"),
]
