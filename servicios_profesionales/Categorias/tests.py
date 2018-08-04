from django.test import TestCase
from django.apps import apps

from .apps import CategoriasConfig

class GalleryViewTests(TestCase):

    def test_apps(self):
        self.assertEqual(CategoriasConfig.name, 'Categorias')
        self.assertEqual(apps.get_app_config('Categorias').name, 'Categorias')
