from django.db import models


class Etudiant(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    email = models.CharField(max_length=150, unique=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    filiere = models.CharField(max_length=100, verbose_name="Filière")
    annee = models.CharField(max_length=10, verbose_name="Année")

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Stage(models.Model):
    """Central model: an internship links a student to a company."""
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]

    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='stages',
        verbose_name="Étudiant",
    )
    entreprise = models.ForeignKey(
        'entreprises.Entreprise',
        on_delete=models.CASCADE,
        related_name='stages',
        verbose_name="Entreprise",
    )
    sujet = models.CharField(max_length=300, verbose_name="Sujet du stage")
    description = models.TextField(blank=True, verbose_name="Description")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_cours',
        verbose_name="Statut",
    )

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
        ordering = ['-date_debut']

    def __str__(self):
        return f"{self.sujet} — {self.etudiant}"