from django import forms
from .models import Etudiant, Stage


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'telephone', 'filiere', 'annee']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control'}),
            'annee': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['etudiant', 'entreprise', 'sujet', 'description', 'date_debut', 'date_fin', 'statut']
        widgets = {
            'etudiant': forms.Select(attrs={'class': 'form-select'}),
            'entreprise': forms.Select(attrs={'class': 'form-select'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.role == 'STUDENT':
            student_qs = Etudiant.objects.filter(email=user.email)
            self.fields['etudiant'].queryset = student_qs
            self.fields['etudiant'].initial = student_qs.first()
            self.fields['etudiant'].widget = forms.HiddenInput()