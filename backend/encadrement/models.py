from django.db import models
from django.conf import settings
from etudiants.models import Stage


class Encadrant(models.Model):
    """
    Profile record for a supervisor (CustomUser with role='SUPERVISOR').

    Why a separate model instead of adding fields to CustomUser?
    The CustomUser model is shared by three roles (STUDENT, SUPERVISOR, COMPANY).
    Putting supervisor-specific fields (department, speciality) there would leave
    those columns NULL for every student and company row — wasted space and a
    broken schema. A dedicated profile model keeps the data clean and decoupled.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='encadrant_profile',
        verbose_name="Compte utilisateur",
    )
    departement = models.CharField(
        max_length=200,
        default='À compléter',
        verbose_name="Département",
    )
    specialite = models.CharField(
        max_length=200,
        default='À compléter',
        verbose_name="Spécialité",
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Biographie / Présentation",
    )

    class Meta:
        verbose_name = "Encadrant"
        verbose_name_plural = "Encadrants"
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Encadrement(models.Model):
    """Supervision assignment: links a supervisor (user) to a specific stage."""
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='encadrements',
        verbose_name="Stage",
    )
    encadrant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='encadrements',
        verbose_name="Encadrant (utilisateur)",
    )
    encadrant_nom = models.CharField(
        max_length=250,
        verbose_name="Nom de l'encadrant",
        help_text="Utilisé si l'encadrant n'a pas de compte utilisateur.",
    )
    role = models.CharField(
        max_length=100,
        blank=True,
        default='Encadrant académique',
        verbose_name="Rôle",
    )
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")

    class Meta:
        verbose_name = "Encadrement"
        verbose_name_plural = "Encadrements"
        ordering = ['-date_debut']

    def __str__(self):
        name = self.encadrant.get_full_name() if self.encadrant else self.encadrant_nom
        return f"{name} → {self.stage}"