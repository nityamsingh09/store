from django import forms
from .models import meme


class memeform(forms.Modelform):
    class Meta:
        model = meme
        fields =['photo','video','title']
