from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import PlatoForm
from comida.models import Plato

def plato_nuevo(request):
    if request.method == "POST":
        formulario = PlatoForm(request.POST)
        if formulario.is_valid():
            plato = formulario.save(commit=False)
            plato = Plato(nombre = formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'])
            plato.save()
        return redirect('plato_nuevo')
    else:
        formulario = PlatoForm()
    return render(request, 'comida/plato_nuevo.html', {'formulario': formulario})
