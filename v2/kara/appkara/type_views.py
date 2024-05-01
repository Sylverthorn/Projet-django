from django.shortcuts import render , HttpResponseRedirect
from .forms import TypeForm
from .models_ import Type
from . import models_

def index(request):
    return render(request, 'type/index.html')

def affiche(request, id):
    type = models_.Type.objects.get(pk = id)
    return render(request, "type/traitement.html", {"type": type})

def saisi(request):
    if request.method == "POST":
        form = TypeForm(request)
        return render(request, 'type/saisi.html', {"form": form})
    else : 
        form = TypeForm()
        return render(request, 'type/saisi.html', {"form": form})
    

def traitement(request):
    form = TypeForm(request.POST)
    if form.is_valid():
        type = form.save()
        return HttpResponseRedirect('/appkara/all_type/')
    else :
        return render(request, 'type/saisi.html', {"form": form})



def update(request, id):
    type = models_.Type.objects.get(pk = id)
    form = TypeForm(type.dico())
    return render(request, "type/saisi.html", {"form": form, "id":id})

def updatetraitement(request, id):
    form = TypeForm(request.POST)
    if form.is_valid():
        type = form.save(commit = False)
        type.id = id
        type.save()
        return HttpResponseRedirect('/appkara/all_type/')
    else :
        return render(request, 'type/saisi.html', {"form": form, "id": id})


def delete(request, id):
    type = models_.Type.objects.get(pk = id)
    type.delete()
    return HttpResponseRedirect('/appkara/all_type/')


def all(request):
    liste = models_.Type.objects.all()
    
    return render(request, "type/all.html", {"liste": liste})

def list():
    liste = models_.Type.objects.all()
    return liste