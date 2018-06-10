from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from usuarios.models import MyUser, Person


# Register your models here.
# para registrar el modelo de usuario personalizado con el administrador de Django se modifica este archivo
class UserCreationForm(forms.ModelForm):
    # Un formulario para crear nuevos usuarios. 
    # Incluye todo lo requerido campos, más una contraseña repetida 
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  # buscar para que sirve widget
    password2 = forms.CharField(label='Password confrmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser  # le estamos diciendo que modelo tiene que usar para crear el formulario
        fields = ('email', 'date_of_birth', 'first_name', 'last_name')

    def clean_password2(self):
        # verifique que las dos entradas de contraseña coinciden
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Guarde la contraseña proporcionada en formato hash
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ Un formulario para actualizar usuarios. Incluye todos los campos
    el usuario, pero reemplaza el campo de contraseña con el de administrador
    campo de visualización de hash de contraseña. """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Independientemente de lo que el usuario proporcione, devuelva el valor inicial.
        # Esto se hace aquí, en lugar de en el campo, porque el
        # campo no tiene acceso al valor inicial
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # los formularios para agregar y cambiar instancias de usuario
    forms = UserChangeForm
    add_form = UserCreationForm

    # Los campos que se usarán para mostrar el modelo de Usuario.
    # Estos reemplazan las definiciones en la base UserAdmin
    # que hacen referencia a campos específicos en auth.User.

    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets no es un atributo ModelAdmin estándar. UserAdmin
    # anula get_fieldsets para usar este atributo al crear un usuario.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    # Ahora registre el nuevo UserAdmin ...
    admin.site.register(MyUser)
    #  admin.site.register(UserAdmin)

    # ... y, dado que no estamos usando los permisos incorporados de Django,
    # anular el registro del modelo de grupo de admin.
    admin.site.unregister(Group)

admin.site.register(Person)
