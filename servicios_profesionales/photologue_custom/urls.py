from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from photologue.models import Photo

from . import views

urlpatterns = [
    path('modificar/<pk>/', login_required(views.UpdateGalleryExtended.as_view()), name="updateGallery"),
    path('modificar/<pk>/photologue/photo/add/',
         CreateView.as_view(model=Photo, fields=['image', 'title', 'slug', 'is_public']), name='add-photo'),
]
