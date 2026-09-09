from django.shortcuts import render

def garaje_view(request):
    """ Vista del Garaje Multimedia """
    return render(request, 'app_deportivos_guadalupe/garaje.html')