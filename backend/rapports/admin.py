from django.contrib import admin
from .models import Rapport


@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    list_display = ('titre', 'stage', 'date_depot')
    search_fields = ('titre', 'stage__sujet', 'stage__etudiant__nom')
    list_filter = ('date_depot',)