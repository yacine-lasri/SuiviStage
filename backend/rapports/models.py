from django.db import models
from etudiants.models import Stage


class Rapport(models.Model):
    """Report submitted for a specific internship."""
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='rapports',
        verbose_name="Stage",
    )
    titre = models.CharField(max_length=250, verbose_name="Titre")
    fichier = models.FileField(upload_to='rapports/', verbose_name="Fichier")
    date_depot = models.DateTimeField(auto_now_add=True, verbose_name="Date de dépôt")

    class Meta:
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"
        ordering = ['-date_depot']

    def __str__(self):
        return f"{self.titre} — {self.stage.etudiant}"