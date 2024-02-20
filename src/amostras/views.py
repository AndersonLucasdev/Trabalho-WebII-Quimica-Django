from django.shortcuts import render, redirect, get_object_or_404
from .forms import AmostraForm
from .forms import Amostra
# Create your views here.

def detalhes_das_amostras(request):
    amostras = Amostra.objects.all()
    return render(request, 'amostras/detalhes_das_amostras.html', {'amostras': amostras})



def criar_amostra(request):
    if request.method == 'POST':
        form = AmostraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_amostras', amostra_id = form.instance.id)
        else:
            form = AmostraForm()
    return render(request, 'amostras/criar_amostra.html', {'form': form})