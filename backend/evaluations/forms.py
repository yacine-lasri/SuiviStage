from django import forms
from .models import Evaluation


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['stage', 'note', 'commentaire']
        widgets = {
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 20, 'step': '0.25'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
