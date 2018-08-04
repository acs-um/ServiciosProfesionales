from django.forms import ModelForm

from photologue.models import Gallery


class GalleryExtendedForm(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
