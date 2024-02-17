from django.shortcuts import render, redirect
from .forms import AmostraForm
# Create your views here.

def criar_amostra(request):
    if request.method == 'POST':
        form = AmostraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_amostras', amostra_id = form.instance.id)
        else:
            form = AmostraForm()
    return render(request, 'amostras/criar_amostra.html', {'form': form})