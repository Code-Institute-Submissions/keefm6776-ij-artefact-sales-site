from django.shortcuts import render, get_object_or_404, redirect
from artefacts.models import Artefact
from .forms import ArtefactForm

# Create your views here.

def all_artefacts(request):
    """ Finds all artefacts in the database and displays them """
    artefacts = Artefact.objects.all()
    return render(request, "artefacts.html", {"artefacts": artefacts})

def artefact_detail(request, pk):
    """ Displays all the artefact details to the user """
    artefact = get_object_or_404(Artefact, pk=pk)
    return render(request, "artefact_detail.html", {"artefact": artefact})

def add_artefact(request):
    """ Allows Site Owner To Add New Artefact To Sell """
    form = ArtefactForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(all_artefacts)
        else:
            form = ArtefactForm()
            return redirect(all_artefacts)
    return render(request, "add_artefact.html", {'form': form})

def edit_artefact_detail(request, pk):
    """ Displays the selected Artefact to the Site Owner for editing """
    artefact = get_object_or_404(Artefact, pk=pk)
    form = ArtefactForm(instance=artefact)
    return render(request, "edit_artefact_detail.html", {'form': form})

def delete_artefact(request, pk):
    """ Allows the Site Owner to delete the current artefact """
    artefact = get_object_or_404(Artefact, pk=pk)
    return redirect(all_artefacts)
