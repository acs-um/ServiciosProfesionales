from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm

from usuarios.models import MyUser, Person


class SignUpForm(ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password', 'password_confirmation', 'first_name', 'last_name']

    def clean_password_confirmation(self):  # confirmamos que lo que ingreso esta bien
        if self.data['password'] != self.data['password_confirmation']:
            raise forms.ValidationError('La contraseña no coincide')
        return self.data['password']

    def clean_email(self):
        user = MyUser.objects.filter(email=self.data['email'])
        if user.exists():
            raise forms.ValidationError('Ya existe un usuario con ese email')
        return self.data['email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['ocupation', 'tel', 'telcel', 'address', 'city', 'state']


class EditPerfil(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password', 'first_name', 'last_name']

    def clean_email(self):
        user = MyUser.objects.filter(email=self.data['email']).exclude(id=self.instance.id)
        if user.exists():
            raise forms.ValidationError('Ya existe un usuario con ese email')
        return self.data['email']


class SetPasswordForm(forms.Form):
    new_password1 = forms.CharField(min_length=6, label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(min_length=6, label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
