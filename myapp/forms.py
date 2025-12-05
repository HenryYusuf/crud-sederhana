from django import forms
from .models import Dokumen

class DokumenForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['judul', 'file']