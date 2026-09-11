from django.shortcuts import render, redirect
from .models import Reporte
from .forms import ReporteForm


def garaje_view(request):
    """ Vista del Garaje Multimedia """
    return render(request, 'app_deportivos_guadalupe/garaje.html')

def evacuacion(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES) #FILES Subidas
        if form.is_valid():
            form.save()
            return redirect('evacuacion')
    else:
        form = ReporteForm()
        reportes = Reporte.objects.all()
        return render(request, 'app_deportivos_guadalupe/evacuacion.html', {
            'form': form,
            'reportes': reportes,
        })