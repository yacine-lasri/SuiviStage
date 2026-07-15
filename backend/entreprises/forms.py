from django import forms
from .models import Entreprise


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'adresse', 'secteur', 'email', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'secteur': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }
