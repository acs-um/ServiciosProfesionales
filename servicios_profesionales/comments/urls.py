from django.conf.urls import include, url
from .views import CommentsCreate, CommentList

urlpatterns = [
    url(r'^listar$', CommentList.as_view(), name="listComments"),
    url(r'^crear$', CommentsCreate.as_view(), name="createComments"),
    #url(r'^modificar/(?P<pk>\d+)/$', views.UpdateService.as_view(), name="updateService"),
    #url(r'^borrar/(?P<pk>\d+)/$', views.DeleteService.as_view(), name="deleteService"),
    #path('ingresar', views.signup, name = "SignUp"),
]