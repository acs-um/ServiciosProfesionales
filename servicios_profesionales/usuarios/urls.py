from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('reset_password', login_required(PasswordResetConfirmView.as_view())),
    path('ingresar/', views.signup, name="SignUp"),
    path('ingresar/login/', views.login, name="EmailLogin"),
    path('', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.get_user_profile, name='update-person'),
    path('cerrar-sesion', views.SignOutView.as_view(), name='sign_out')
]
