from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Comment
from servicios.models import Service
from django.urls import reverse
from django import forms
from .form import CommentForm
# Create your views here.


class CommentList(ListView):
    model = Comment
    template_name = 'comments/listComments.html'


class CommentsCreate(CreateView):
    print("Entraste perro1")
    model = Comment
    fields = '__all__'
    form = CommentForm()
    template_name = "comments/createComments.html"

    def get_success_url(self):
        print("Entraste perro2")
        return reverse('listComments')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.created_by = self.request.user
        comment.save()
        print("Entraste perro3")
        return super(CommentsCreate, self).form_valid(form)
