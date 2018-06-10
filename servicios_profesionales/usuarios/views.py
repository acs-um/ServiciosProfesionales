from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  # para la anotacion de loguin_required
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SignUpForm, EditPerfil, SetPasswordForm, UserProfileForm, ProfileUpdateView
from .models import MyUser, Person
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.conf import urls
from servicios.models import Service
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView
from .forms import UserProfileForm
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


def updateUser(UpdateView):
    model = MyUser
    fields = '___add___'
    form = ProfileUpdateView()
    template_name = ''


class SignOutView(LogoutView):
    pass


def get_user_profile(request):
    user = MyUser.objects.get(email=request.user.email)
    person = Person.objects.get(user=user)
    service = Service.objects.filter(myuser=user)
    return render(request, 'accounts/profile/index.html', {"person": person, "services": service})


class ProfileObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = MyUser

    def get_object(self):
        """Return's the current users profile."""
        try:
            return self.request.user.get_profile()
        except MyUser.DoesNotExist:
            raise NotImplemented(
                "What if the user doesn't have an associated profile?")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        klass = ProfileObjectMixin
        return super(klass, self).dispatch(request, *args, **kwargs)


class ProfileUpdateView(ProfileObjectMixin, UpdateView):
    """
    A view that displays a form for editing a user's profile.

    Uses a form dynamically created for the `Profile` model and
    the default model's update template.
    """
    pass  # That's All Folks!
