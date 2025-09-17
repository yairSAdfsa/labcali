from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm

# Listar
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar.html', {'mascotas': mascotas})

# Crear
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'crear.html', {'form': form})

# Editar
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'editar.html', {'form': form})

# Eliminar
def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listar_mascotas')
    return render(request, 'eliminar.html', {'mascota': mascota})