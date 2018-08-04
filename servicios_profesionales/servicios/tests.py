from django.urls import reverse, resolve
from django.test import TestCase
from django.apps import apps

from servicios.apps import ServiciosConfig
from servicios.form import ServiceForm
from servicios.models import Service
from Categorias.models import Categoria
from usuarios.models import MyUser, Person


class ServiceViewTests(TestCase):

    def setUp(self):
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
        self.categoria2 = Categoria.objects.create(
            name='Plomería',
            description='Trabajos de plomería')
        self.service = Service.objects.create(
            name='Albañil',
            description='Servicios generales',
            category=self.categoria
        )
        self.service2 = Service.objects.create(
            name='Yesero',
            description='Yesería en general',
            category=self.categoria
        )

    def test_apps(self):
        self.assertEqual(ServiciosConfig.name, 'servicios')
        self.assertEqual(apps.get_app_config('servicios').name, 'servicios')

    def test_service_list(self):
        resp = self.client.get(reverse('all-services'))
        self.assertEqual(resp.status_code, 200)

        # que los servicios estén en el contexto
        self.assertEqual(resp.context["service_list"].count(), 2)
        self.assertTrue(self.service in resp.context["service_list"])
        self.assertTrue(self.service2 in resp.context["service_list"])

        # que los nombres de los servicios estén en el html
        self.assertContains(resp, self.service.name)
        self.assertContains(resp, self.service2.name)

    def test_service_search(self):
        resp = self.client.get(reverse('all-services'), {'search': self.service2.name})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["service_list"].count(), 1)
        self.assertContains(resp, self.service2.name)

    def test_form_service(self):
        form = ServiceForm(data={
            'name': self.service2.name,
            'description': self.service2.description,
            'category': self.categoria.id,
            'tags': "futurma",
        })
        self.assertTrue(form.is_valid())
        service = form.save()
        resp = self.client.get(reverse('all-services'))
        self.assertTrue(service in resp.context["service_list"])

    def test_create_service(self):
        form = ServiceForm(data={
            'name': self.service2.name,
            'description': self.service2.description,
            'category': self.categoria.id,
            'tags': "futurma",
        })
        self.assertTrue(form.is_valid())
        self.client.login(username=self.user.email, password=self.user.password)
        response = self.client.post(reverse('createService'), {'form': form})
        self.assertEqual(response.status_code, 200)

    def test_update_service(self):
        form = ServiceForm(data={
            'name': self.service2.name,
            'description': self.service2.description,
            'category': self.categoria.id,
            'tags': "futurma",
        })
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('updateService', kwargs={'pk': self.service.id}), {'form': form})
        self.assertEqual(response.status_code, 302)

    def test_delete_service(self):
        response = self.client.post(reverse('deleteService', kwargs={'pk': self.service.id}))
        self.assertEqual(response.status_code, 302)
