from django import forms
from .models import *


class ImgForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'image']
