from django.contrib import admin
from .models import Evaluation


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('stage', 'note', 'date_evaluation')
    search_fields = ('stage__sujet', 'stage__etudiant__nom')
    list_filter = ('date_evaluation',)