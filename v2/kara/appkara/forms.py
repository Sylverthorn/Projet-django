from django.forms import ModelForm 
from django.utils.translation import gettext_lazy as _ 
from . import models_


class TechniqueForm(ModelForm):
    class Meta :
        model = models_.Technique
        fields = ('nom', 'description', 'type')
       
        labels = {
            'nom' : _('Nom'),
            'description' : _('Description'),
            'type' : _('Type')
        }

class TypeForm(ModelForm):
    class Meta :
        model = models_.Type
        fields = ('type',)
       
        labels = {
            'type' : _('Type')
        }