from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.apps import apps

from .apps import PhotologueCustomConfig
from .form import GalleryExtendedForm
from Categorias.models import Categoria
from .models import GalleryExtended
from usuarios.models import MyUser
from servicios.models import Service
from photologue.models import Photo


class GalleryViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
            email=" test@g.com ",
            date_of_birth="1995-01-02",
            password=" 123123b ",
            first_name="Test",
            last_name="Apellido"
        )
        self.categoria = Categoria.objects.create(
            name='Construcción',
            description='Trabajos de construcción'
        )
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
        self.assertEqual(PhotologueCustomConfig.name, 'photologue_custom')
        self.assertEqual(apps.get_app_config('photologue_custom').name, 'photologue_custom')

    def test_gallery(self):
        custom_g = GalleryExtended.nuevo(self.service, self.user)
        string = self.user.first_name + '-' + self.service.name
        self.assertEquals(custom_g.gallery.title, string)
        form = GalleryExtendedForm(data={
            'title': custom_g.gallery.title, 'slug': custom_g.gallery.slug,
            'description': custom_g.gallery.description,
        })
        self.assertFalse(form.is_valid())

    def test_update_gallery(self):
        galeria = GalleryExtended.nuevo(self.service2, self.user)
        pc = galeria.gallery.photo_count()
        p1 = Photo.objects.create(title='test photo 1')
        galeria.gallery.photos.add(p1)
        str = galeria.gallery.photo_count()
        response = self.client.post(
            reverse('updateGallery', kwargs={'pk': galeria.gallery.id}),
            {'photos': p1})
        self.assertEqual(response.status_code, 302)
        galeria.refresh_from_db()
        self.assertEqual(pc + 1, galeria.gallery.photo_count())
        description = "The Catcher in the Rye"
        response = self.client.post(
            reverse('updateGallery', kwargs={'pk': galeria.gallery.id}),
            {'description': description, 'photos': p1})
        self.assertEqual(response.status_code, 302)
