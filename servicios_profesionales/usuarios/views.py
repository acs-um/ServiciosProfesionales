from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #para la anotacion de loguin_required
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.views import generic
from .forms import SignUpForm, EditPerfil, SetPasswordForm
from .models import MyUser


from django.contrib.auth.views import login

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Save new user attributes
            form.save()

            return HttpResponseRedirect("/ingresar/")  # Redirect after POST

    else:
        form = SignUpForm()
    data = {
        'form': form,
    }

    return render(request, 'usuarios/signup.html', data)
