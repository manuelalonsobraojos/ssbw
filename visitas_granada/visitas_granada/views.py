from django.shortcuts import render, redirect
from django.template.loader  import get_template
from visitas_granada.models import Visita, Comentario, VisitaForm
from django.contrib.auth.decorators import login_required
import os

def index(request):

    visits = Visita.objects.all()
    return render(request, 'index.html', {'visits': visits})

def getVisit(request, visit_id):

    visit = Visita.objects.get(id=visit_id)
    coments = Comentario.objects.filter(visita=visit_id)
    return render(request, 'visit.html', {'visit': visit, 'coments': coments})

@login_required
def newVisitView(request):
    form = VisitaForm()

    return render(request, "new_visit.html", {'form': form})

@login_required
def addVisit(request):
    form = VisitaForm()

    if request.method == 'POST':  # de vuelta con los datos

        form = VisitaForm(request.POST, request.FILES)  # bound the form

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form
        }
    # GET o error
    return render(request, "new_visit.html", context)

@login_required
def editVisitView(request, visit_id):
    visit = Visita.objects.get(pk=visit_id)
    form = VisitaForm(instance=visit)

    return render(request, "edit_visit.html", {'form': form, 'visit':visit})

@login_required
def editVisit(request, visit_id):
    visit = Visita.objects.get(pk=visit_id)
    form = VisitaForm(instance=visit)

    if request.method == 'POST':  # de vuelta con los datos

        form = VisitaForm(request.POST, request.FILES, initial=visit.__dict__, instance=visit)  # bound the form

        if form.is_valid():
            if form.has_changed():
                form.save()
            return redirect('index')

        context = {
            'form': form
        }
    # GET o error
    return render(request, "edit_visit.html", context)

@login_required
def deleteVisit(request, visit_id):
    visit = Visita.objects.get(pk=visit_id)
    visit.delete()
    return redirect('index')