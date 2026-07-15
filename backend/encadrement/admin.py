from django.contrib import admin
from .models import Encadrant, Encadrement


@admin.register(Encadrant)
class EncadrantAdmin(admin.ModelAdmin):
    """
    Displays the supervisor profile table.
    The admin can see which CustomUser accounts have a supervisor profile,
    edit their department/speciality, and spot any profiles with placeholder values
    that need completing.
    """
    list_display = ('__str__', 'get_email', 'departement', 'specialite')
    search_fields = ('user__username', 'user__email', 'user__first_name',
                     'user__last_name', 'departement', 'specialite')
    list_filter = ('departement',)
    raw_id_fields = ('user',)  # Avoids loading all users into a dropdown

    @admin.display(description='Email')
    def get_email(self, obj):
        return obj.user.email


@admin.register(Encadrement)
class EncadrementAdmin(admin.ModelAdmin):
    """
    Displays the bridge/assignment table that links a supervisor to a stage.
    This is the primary tool the admin uses to assign internships to supervisors.
    """
    list_display = ('stage', 'encadrant', 'encadrant_nom', 'role',
                    'date_debut', 'date_fin')
    search_fields = ('encadrant_nom', 'stage__sujet',
                     'encadrant__username', 'encadrant__email')
    list_filter = ('role', 'date_debut')
    autocomplete_fields = ('stage',)   # Fast search for stages in the dropdown
    date_hierarchy = 'date_debut'