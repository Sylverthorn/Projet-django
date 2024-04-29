from django.forms import ModelForm 
from django.utils.translation import gettext_lazy as _ 
from . import models


class TechniqueForm(ModelForm):
    class Meta :
        model = models.Technique
        fields = ('nom', 'description', 'type')
       
        labels = {
            'nom' : _('Nom'),
            'description' : _('Description'),
            'type' : _('Type')
        }