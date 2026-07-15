from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):

    # ── Role choices ──────────────────────────────────────────
    # Admin is NOT a role — the admin is a Django superuser
    # created via: python manage.py createsuperuser
    STUDENT = 'STUDENT'
    SUPERVISOR = 'SUPERVISOR'
    COMPANY = 'COMPANY'

    ROLE_CHOICES = [
        (STUDENT, 'Étudiant'),
        (SUPERVISOR, 'Encadrant'),
        (COMPANY, 'Entreprise'),
    ]

    # ── Fields ────────────────────────────────────────────────
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=STUDENT,
        verbose_name="Rôle",
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    address = models.TextField(blank=True, verbose_name="Adresse")

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    # ── Helper methods ────────────────────────────────────────
    def is_student(self):
        return self.role == self.STUDENT

    def is_supervisor(self):
        return self.role == self.SUPERVISOR

    def is_company(self):
        return self.role == self.COMPANY


# ── Signals ───────────────────────────────────────────────────────────────────
# Auto-create a matching Etudiant or Entreprise profile whenever a new
# CustomUser account is registered. This prevents "ghost profiles" where a
# user logs in but has no linked domain record, causing crashes in HomeView.

@receiver(post_save, sender=CustomUser)
def create_profile_on_signup(sender, instance, created, **kwargs):
    """
    Fires once, immediately after a new CustomUser row is INSERT-ed.
    `created=True` only on INSERT, not on every UPDATE save.

    Role → Profile mapping:
        STUDENT    → etudiants.Etudiant   (academic identity)
        SUPERVISOR → encadrement.Encadrant (supervisor profile)
        COMPANY    → entreprises.Entreprise (company profile)
        superuser  → no profile row needed (uses Django admin directly)
    """
    if not created or instance.is_superuser:
        return

    if instance.role == CustomUser.STUDENT:
        # Import here to avoid circular imports (users ← etudiants ← users)
        from etudiants.models import Etudiant
        import datetime
        Etudiant.objects.get_or_create(
            email=instance.email,
            defaults={
                'nom': instance.last_name or instance.username,
                'prenom': instance.first_name or instance.username,
                'telephone': instance.phone,
                'filiere': 'À compléter',
                'annee': str(datetime.date.today().year),
            }
        )

    elif instance.role == CustomUser.SUPERVISOR:
        # Import here to avoid circular imports (users ← encadrement ← etudiants ← users)
        from encadrement.models import Encadrant
        Encadrant.objects.get_or_create(
            user=instance,
            defaults={
                'departement': 'À compléter',
                'specialite': 'À compléter',
                'bio': '',
            }
        )

    elif instance.role == CustomUser.COMPANY:
        # Import here to avoid circular imports
        from entreprises.models import Entreprise
        Entreprise.objects.get_or_create(
            email=instance.email,
            defaults={
                'nom': instance.get_full_name() or instance.username,
                'adresse': instance.address or 'À compléter',
                'secteur': 'À compléter',
                'telephone': instance.phone,
            }
        )


