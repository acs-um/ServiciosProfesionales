from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView
from . import views
from django.conf.urls import url
urlpatterns = [
    path('reset_password', PasswordResetConfirmView.as_view()),
   # path('ingresar', views.signup, name = "SignUp"),
    url(r'^ingresar/$', views.signup, name="SignUp"),
]
