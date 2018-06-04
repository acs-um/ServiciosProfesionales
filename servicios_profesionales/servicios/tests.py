from django.urls import reverse
from django.test import TestCase


from servicios.models import Service
from Categorias.models import Categoria

class ServiceViewTests(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            name='Construcción',
            description='Trabajos de construcción')
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
        resp = self.client.get(resolve())
        self.assertEqual(resp.status_code, 200)
