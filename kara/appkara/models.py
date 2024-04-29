from django.db import models
from django import forms

CHOICES = {
    "Blocage": "Blocage",
    "Technique de poing": "Technique de poing",
    "Technique de jambe": "Technique de jambe",
    "Position": "Position",
}
# Create your models here.


class Technique(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    type = models.CharField(
        max_length=100,
        choices=CHOICES,
        default="uke",
    )
    def __str__(self):
        chaine = f"""{self.nom}-----{self.type}-----{self.description}"""
        return chaine
    