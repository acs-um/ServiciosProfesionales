from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all-services"),
    #path('ingresar', views.signup, name = "SignUp"),
]