from django.shortcuts import render , HttpResponseRedirect
from .forms import TechniqueForm
from .models import Technique
from . import models
# Create your views here.

def index(request):
    return render(request, 'appkara/index.html')


def all(request):
    liste = list(models.Technique.objects.all())
    return render(request, "appkara/all.html", {"liste": liste})

def affiche(request, id):
    technique = models.Technique.objects.get(pk = id)
    return render(request, "appkara/traitement.html", {"technique": technique})

def saisi(request):
    if request.method == "POST":
        form = TechniqueForm(request)
        return render(request, 'appkara/saisi.html', {"form": form})
    else : 
        form = TechniqueForm()
        return render(request, 'appkara/saisi.html', {"form": form})
    

def traitement(request):
    form = TechniqueForm(request.POST)
    if form.is_valid():
        technique = form.save()
        return HttpResponseRedirect('/appkara/all/')
    else :
        return render(request, 'appkara/saisi.html', {"form": form})



def update(request, id):
    technique = models.Technique.objects.get(pk = id)
    form = TechniqueForm(technique.dico())
    return render(request, "appkara/saisi.html", {"form": form, "id":id})

def updatetraitement(request, id):
    form = TechniqueForm(request.POST)
    if form.is_valid():
        technique = form.save(commit = False)
        technique.id = id
        technique.save()
        return HttpResponseRedirect('/appkara/all/')
    else :
        return render(request, 'appkara/saisi.html', {"form": form, "id": id})


def delete(request, id):
    technique = models.Technique.objects.get(pk = id)
    technique.delete()
    return HttpResponseRedirect('/appkara/all/')


#filter àFAIRE
def type_filter(request, type):
    liste = list(models.Technique.objects.all().filter( type = type))
    return render(request, "appkara/all.html", {"liste": liste})