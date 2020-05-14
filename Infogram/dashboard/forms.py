from django import forms
from .models import PublicacionBien
from usuarios.models import User


class PublicacionForm(forms.ModelForm):
    imagen = forms.ImageField()
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:
        model = PublicacionBien
        fields = ['user', 'imagen', 'descripcion']