from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.conf import urls
from django.views.generic import UpdateView
from django.contrib.auth.views import login

from .forms import SignUpForm, UserProfileForm
from .models import Person


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Save new user attributes
            user = form.save()
            p = Person()
            p.setUser(user)
            p.save()
            return HttpResponseRedirect('http://localhost:8000/usuarios/login/')  # Redirect after POST

    else:
        form = SignUpForm()
    data = {
        'form': form,
    }

    return render(request, 'usuarios/signup.html', data)


def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['email'],
            password=request.POST['password']
        )
        request.session[user.id]
        print(request.session[user.id])
        if user is not None:
            login(request, user)
            return redirect(urls.handler500)


class SignOutView(LogoutView):
    pass


def get_user_profile(request):
    person = Person.objects.get(user=request.user)
    return render(request, 'accounts/profile/index.html',
                  {"person": person,
                   "services": request.user.service_set.all(),
                   "gallery_list": request.user.galleryextended_set.all()})


class UpdatePerson(UpdateView):
    model = Person
    form = UserProfileForm()
    form_class = UserProfileForm
    template_name = 'accounts/profile/updatePerson.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('personDetails')
