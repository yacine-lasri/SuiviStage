from django.db import models


class Entreprise(models.Model):
    nom = models.CharField(max_length=250, verbose_name="Nom")
    adresse = models.TextField(verbose_name="Adresse")
    secteur = models.CharField(max_length=250, verbose_name="Secteur d'activité")
    email = models.EmailField(blank=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"
        ordering = ['nom']

    def __str__(self):
        return self.nom