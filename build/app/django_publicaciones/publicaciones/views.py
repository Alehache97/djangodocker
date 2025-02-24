from django.shortcuts import render, redirect
from .models import Publicacion
from .forms import PublicacionForm

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()

    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')  # Redirigir después de enviar
    else:
        form = PublicacionForm()

    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones, 'form': form})
