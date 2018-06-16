from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Comment
from servicios.models import Service
from django.urls import reverse
from django import forms
from .form import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
# Create your views here.


class CommentList(ListView):
    model = Comment
    template_name = 'comments/listComments.html'


class CommentsCreate(CreateView):
    print("Entraste 1")
    model = Comment
    form_class = CommentForm
    template_name = "comments/createComments.html"
  
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.created_by = self.request.user
        comment.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        print("Entraste 3")
        return reverse('listComments')
