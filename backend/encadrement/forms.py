from django import forms
from .models import Encadrement


class EncadrementForm(forms.ModelForm):
    class Meta:
        model = Encadrement
        fields = ['stage', 'encadrant', 'encadrant_nom', 'role', 'date_debut', 'date_fin']
        widgets = {
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'encadrant': forms.Select(attrs={'class': 'form-select'}),
            'encadrant_nom': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
