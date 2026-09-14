from django.shortcuts import render, redirect
from .models import Reporte
from .forms import ReporteForm


def garaje_view(request):
    """ Vista del Garaje Multimedia """
    return render(request, 'app_deportivos_guadalupe/garaje.html')

def evacuacion(request):
    reportes = Reporte.objects.all()

    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES) #FILES Subidas
        if form.is_valid():
            form.save()
            return redirect('app_deportivos_guadalupe:features_test')
    else:
        form = ReporteForm()

    return render(request, 'app_deportivos_guadalupe/features-test-dp.html', {
        'form': form,
        'reportes': reportes,
    })