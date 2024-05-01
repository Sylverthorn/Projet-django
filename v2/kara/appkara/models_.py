from django.db import models
from .type_views import list


CHOICES = list()
g = {
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
        default="NONE",
    )
    def __str__(self):
        chaine = f"""{self.nom}-----{self.type}-----{self.description}"""
        return chaine

    def dico(self):
        return {"nom":self.nom, "description":self.description, "type":self.type}
    

class Type(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        chaine = f"""{self.type}"""
        return chaine

    def dico(self):
        return {"type":self.type}