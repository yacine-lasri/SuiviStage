from django import forms
from .models import Rapport


class RapportForm(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = ['stage', 'titre', 'fichier']
        widgets = {
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'fichier': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
