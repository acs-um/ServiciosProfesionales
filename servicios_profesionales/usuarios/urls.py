from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('reset_password', login_required(PasswordResetConfirmView.as_view())),
    path('ingresar/', views.signup, name="SignUp"),
    path('ingresar/login/', views.login, name="EmailLogin"),
    path('', include('django.contrib.auth.urls')),
    path('accounts/profile/', login_required(views.get_user_profile), name='personDetails'),
    path('accounts/profile/<pk>/', login_required(views.UpdatePerson.as_view()), name='UpdatePerson'),
    path('cerrar-sesion', login_required(views.SignOutView.as_view()), name='sign_out')
]
