from django.forms import ModelForm
from .models import GalleryExtended


class GalleryExtendedForm(ModelForm):
    class Meta:
        model = GalleryExtended
        fields = '__all__'
