from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView
from . import views

urlpatterns = [
    path('reset_password', PasswordResetConfirmView.as_view()),
    path('ingresar', views.signup, name = "SignUp"),
]
