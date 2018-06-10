from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Comment
from servicios.models import Service
from django.urls import reverse
from django import forms
from .form import CommentForm
# Create your views here.
"""class ServiceCommentList(ListView):
    context_object_name = Comment
    template_name = 'comments/comments_by_publisher.html/'
    def get_queryset(self):
        self.service = get_object_or_404(Service, name=self.kwargs['service'])
        return Comment.objects.filter(service=self.service)"""

class CommentsCreate(CreateView):
    model = Comment
    fields = '__all__'
    form = CommentForm()
    template_name = "comments/createComments.html"

    def get_success_url(self):
        return reverse('listComments')