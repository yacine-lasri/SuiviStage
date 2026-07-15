from django.contrib import admin
from .models import Entreprise

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'email', 'telephone')
    search_fields = ('nom', 'secteur')