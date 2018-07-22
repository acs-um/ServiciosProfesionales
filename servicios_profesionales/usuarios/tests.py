from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve

from Categorias.models import Categoria
from .forms import SignUpForm
from .models import MyUser, Person
from servicios.models import Service
from .backends import EmailAuth


# Comprobando la vista del signUp
class SignUpViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
            email="test@g.com",
            date_of_birth="1995-01-02",
            password="123123b",
            first_name="Test",
            last_name="Apellido"
        )
        self.person = Person.objects.create(
            user=self.user
        )
        self.categoria = Categoria.objects.create(
            name='Construcción',
            description='Trabajos de construcción')
        self.service = Service.objects.create(
            name='Albañil',
            description='Servicios generales',
            category=self.categoria
        )

    def test_db_user(self):
        # Se comprueba que haya sido creado en la tabla Usuario
        self.assertEqual(MyUser.objects.filter(email="test@g.com").count(), 1)

    def test_login(self):
        # should be logged in now
        self.assertEqual(EmailAuth.authenticate(self, self.user.email, self.user.password), self.user)
        self.assertEqual(EmailAuth.authenticate(self, 'asd', self.user.password), None)
        self.assertEqual(EmailAuth.get_user(self, self.user.id), self.user)
        self.assertEqual(EmailAuth.get_user(self, 505), None)
        self.client.login(username=self.user.email, password=self.user.password)
        response = self.client.post(reverse('personDetails'))
        self.assertEqual(response.status_code, 200)

    """def get_user_profile(self):
        response = self.client.post.reverse('personDetails')
        self.assertContains(Service in response.context)
        self.assertContains(Gallery in response.context)
        self.assertContains(Person in response.context)

    def person_test_form(self):
        form = UserProfileForm(data={
            'ocupation': 'test_ocupation',
            'tel': '123456789',
            'telcel': '987654321',
            'address': 'test_address',
            'city': 'city_test',
            'state': 'state_test',
        })
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('UpdatePerson'), {'form': form})
        self.assertEqual(response.status_code, 200)"""


class SignUpTest(TestCase):
    def test_signup_templates_used(self):
        # testeamos que usamos el template 'usuarios/signup.html'
        response = self.client.get(reverse('SignUp'))  # Que puede ir aca!?????
        self.assertTemplateUsed(response, 'usuarios/signup.html')

    def test_signup_view(self):
        # datos en context de la vista
        # por get, llega el form.
        response = self.client.get(reverse('SignUp'))
        self.assertTrue("form" in response.context)
        self.assertTrue(isinstance(response.context["form"], SignUpForm))

    def test_signup_post(self):
        # Que llegan los datos bien por POST
        # que se crea un user nuevo en la db
        # Intento crear un usuario sin setear un campo obligatorio, para probarlo hay q comentar email
        form = SignUpForm(data={
            'email': "tessdt@g.com",
            'date_of_birth': "1995-01-02",
            'password': "123123b",
            'password_confirmation': "123123b",
            'first_name': "Test",
            'last_name': "Apellido",
        })
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('SignUp'), {form: form})
        self.assertEqual(response.status_code, 200)
        # Se comprueba que haya sido creado en la tabla User
        # self.assertEqual(MyUser.objects.get(email="tessdt@g.com").count(), 1)
