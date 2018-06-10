from django.db import models
from servicios.models import Service
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, AbstractUser)


class MyUserManager(BaseUserManager):  # maneja mi user en la bd
    # use_in_migrations = True

    def create_user(self, email, date_of_birth, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )  # para que sea unico
    date_of_birth = models.DateTimeField()
    first_name = models.CharField(
        verbose_name='first_name',
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=30,
        blank=True,
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)

    is_active = models.BooleanField(
        default=True)  # atributo que devuelve True si la cuenta de usuario está actualmente activa.
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'  # lo que vamos a usar como identificador unico
    REQUIRED_FIELDS = ['date_of_birth', 'first_name',
                       'last_name']  # una lista de los nombres de campo que se solicitarán al crear un usuario a través del createsuperusercomando de administración

    def __str__(self):
        return self.email

    def setService(self, service):
        self.service = service
        return self.save()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self,
                         app_label):  # True si el usuario tiene permiso para acceder a los modelos en la aplicación determinada.
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):  # True si el usuario tiene permiso para acceder al sitio de administración.
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager
class Person(models.Model):
    ocupation = models.CharField(
        verbose_name='Ocupation',
        max_length=50,
        null=True
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tel = models.CharField(
        verbose_name='Telephone number',
        max_length=30,
        null=False
    )
    telcel = models.CharField(
        verbose_name='Telephone number',
        max_length=30,
        null=True
    )
    address = models.CharField(
        verbose_name='Your address',
        max_length=40,
        null=False
    )
    city = models.CharField(
        verbose_name='City',
        max_length=40,
        null=False
    )
    state = models.CharField(
        verbose_name='State',
        max_length=40,
        null=False
    )
    photo = models.ImageField
