from django.db import models
from etudiants.models import Stage


class Evaluation(models.Model):
    """Grade/evaluation tied to a specific internship."""
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='evaluations',
        verbose_name="Stage",
    )
    note = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Note")
    commentaire = models.TextField(blank=True, verbose_name="Commentaire")
    date_evaluation = models.DateTimeField(auto_now_add=True, verbose_name="Date d'évaluation")

    class Meta:
        verbose_name = "Évaluation"
        verbose_name_plural = "Évaluations"
        ordering = ['-date_evaluation']

    def __str__(self):
        return f"{self.stage.etudiant} — {self.note}/20"