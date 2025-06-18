from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formulario/sucesso.html')
    else:
        form = ContatoForm()
    return render(request, 'formulario/index.html', {'form': form})
