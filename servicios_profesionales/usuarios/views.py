from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  # para la anotacion de loguin_required
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SignUpForm, EditPerfil, SetPasswordForm, UserProfileForm
from .models import MyUser, Person
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.conf import urls
from servicios.models import Service
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView, FormView
from django.contrib.auth.views import login


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
    user = MyUser.objects.get(email=request.user.email)
    person = Person.objects.get(user=user)
    service = Service.objects.filter(myuser=user)
    return render(request, 'accounts/profile/index.html', {"person": person, "services": service})


class UpdatePerson(UpdateView):
    model = Person
    form = UserProfileForm()
    form_class = UserProfileForm
    template_name = 'accounts/profile/updatePerson.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('personDetails')
