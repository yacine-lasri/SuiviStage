from django.contrib import admin
from .models import Etudiant, Stage


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'filiere', 'annee')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('filiere', 'annee')


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'etudiant', 'entreprise', 'date_debut', 'date_fin', 'statut')
    search_fields = ('sujet', 'etudiant__nom', 'entreprise__nom')
    list_filter = ('statut', 'date_debut')