from django.test import TestCase
from django.apps import apps

from .apps import ComentariosConfig


class GalleryViewTests(TestCase):
    def test_apps(self):
        self.assertEqual(ComentariosConfig.name, 'comentarios')
        self.assertEqual(apps.get_app_config('comentarios').name, 'comentarios')
