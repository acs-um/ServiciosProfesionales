from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all-services"),
    #url(r'^search/$', views.search, name="search-service"),
]