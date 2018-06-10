"""servicios_profesionales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from photologue.models import Photo
from photologue_custom import views
from usuarios import urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^usuarios/', include('usuarios.urls')),
                  url(r'^comentario/', include('comments.urls')),
                  path('photologue/photo/add/', CreateView.as_view(model=Photo, fields='__all__'), name='add-photo'),
                  path('modificar/<pk>/', login_required(views.UpdateGalleryExtended.as_view()), name="updateGallery"),
                  path('photologue/', include('photologue.urls', namespace='photologue'), name='photologue'),
                  url(r'^servicios/', include('servicios.urls')),
                  url(r'^gallery_extended/', include('photologue_custom.urls')),
                  url(r'^$', TemplateView.as_view(template_name='index.html')),
                  url(r'^media/(?P<path>.*)$', serve, {
                      'document_root': settings.MEDIA_ROOT,
                  }),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
