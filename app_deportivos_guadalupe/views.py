import json
from decimal import Decimal, InvalidOperation

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Reporte, Trayectoria, Ubicacion
from .forms import ReporteForm


def garaje_view(request):
    """ Vista del Garaje Multimedia """
    return render(request, 'app_deportivos_guadalupe/garaje.html')

def mapa_view(request):
    return render(request, 'app_deportivos_guadalupe/features-test-maps.html')


def _json_body(request):
    try:
        return json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return None


def _decimal(value):
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return None


def _ubicacion_data(ubicacion):
    return {
        'id': ubicacion.id,
        'nombre': ubicacion.nombre,
        'descripcion': ubicacion.descripcion,
        'tamano_sede': ubicacion.tamano_sede,
        'direccion': ubicacion.direccion,
        'latitud': float(ubicacion.latitud),
        'longitud': float(ubicacion.longitud),
        'fecha_creacion': ubicacion.fecha_creacion.isoformat(),
    }


def _trayectoria_data(trayectoria):
    return {
        'id': trayectoria.id,
        'nombre': trayectoria.nombre,
        'puntos': trayectoria.puntos,
        'geometria': trayectoria.geometria,
        'fecha_creacion': trayectoria.fecha_creacion.isoformat(),
    }


@require_http_methods(['GET', 'POST'])
def ubicaciones_api(request):
    if request.method == 'GET':
        return JsonResponse({'ubicaciones': [_ubicacion_data(item) for item in Ubicacion.objects.all()]})

    data = _json_body(request)
    latitud = _decimal(data.get('latitud')) if data else None
    longitud = _decimal(data.get('longitud')) if data else None
    required = ['nombre', 'tamano_sede', 'direccion']
    if not data or any(not str(data.get(field, '')).strip() for field in required) or latitud is None or longitud is None:
        return JsonResponse({'error': 'Completa los datos de la ubicación y sus coordenadas.'}, status=400)

    ubicacion = Ubicacion.objects.create(
        nombre=data['nombre'].strip(),
        descripcion=str(data.get('descripcion', '')).strip(),
        tamano_sede=data['tamano_sede'],
        direccion=data['direccion'].strip(),
        latitud=latitud,
        longitud=longitud,
    )
    return JsonResponse(_ubicacion_data(ubicacion), status=201)


@require_http_methods(['PUT', 'DELETE'])
def ubicacion_api(request, ubicacion_id):
    try:
        ubicacion = Ubicacion.objects.get(pk=ubicacion_id)
    except Ubicacion.DoesNotExist:
        return JsonResponse({'error': 'Ubicación no encontrada.'}, status=404)

    if request.method == 'DELETE':
        ubicacion.delete()
        return JsonResponse({'deleted': True})

    data = _json_body(request)
    if not data or not str(data.get('nombre', '')).strip() or not str(data.get('direccion', '')).strip():
        return JsonResponse({'error': 'El nombre y la dirección son obligatorios.'}, status=400)
    ubicacion.nombre = data['nombre'].strip()
    ubicacion.descripcion = str(data.get('descripcion', '')).strip()
    ubicacion.tamano_sede = data.get('tamano_sede', ubicacion.tamano_sede)
    ubicacion.direccion = data['direccion'].strip()
    latitud = _decimal(data.get('latitud', ubicacion.latitud))
    longitud = _decimal(data.get('longitud', ubicacion.longitud))
    if latitud is None or longitud is None:
        return JsonResponse({'error': 'Las coordenadas no son válidas.'}, status=400)
    ubicacion.latitud = latitud
    ubicacion.longitud = longitud
    ubicacion.save()
    return JsonResponse(_ubicacion_data(ubicacion))


@require_http_methods(['GET', 'POST'])
def trayectorias_api(request):
    if request.method == 'GET':
        return JsonResponse({'rutas': [_trayectoria_data(item) for item in Trayectoria.objects.all()]})

    data = _json_body(request)
    puntos = data.get('puntos') if data else None
    geometria = data.get('geometria') if data else None
    if not data or not str(data.get('nombre', '')).strip() or not isinstance(puntos, list) or len(puntos) < 2 or not isinstance(geometria, list):
        return JsonResponse({'error': 'Una ruta necesita nombre, al menos dos puntos y una geometría.'}, status=400)
    trayectoria = Trayectoria.objects.create(nombre=data['nombre'].strip(), puntos=puntos, geometria=geometria)
    return JsonResponse(_trayectoria_data(trayectoria), status=201)


@require_http_methods(['PUT', 'DELETE'])
def trayectoria_api(request, trayectoria_id):
    try:
        trayectoria = Trayectoria.objects.get(pk=trayectoria_id)
    except Trayectoria.DoesNotExist:
        return JsonResponse({'error': 'Ruta no encontrada.'}, status=404)
    if request.method == 'DELETE':
        trayectoria.delete()
        return JsonResponse({'deleted': True})
    data = _json_body(request)
    if not data or not str(data.get('nombre', '')).strip():
        return JsonResponse({'error': 'El nombre de la ruta es obligatorio.'}, status=400)
    trayectoria.nombre = data['nombre'].strip()
    trayectoria.save()
    return JsonResponse(_trayectoria_data(trayectoria))

def solicitudes_adicion_view(request):
    reportes = Reporte.objects.all()

    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES) #FILES Subidas
        if form.is_valid():
            form.save()
            return redirect('app_deportivos_guadalupe:feat_soliadds')
    else:
        form = ReporteForm()

    return render(request, 'app_deportivos_guadalupe/features-test-SoliciAdds.html', {
        'form': form,
        'reportes': reportes,
    })

def evacuacion(request):
    return redirect('app_deportivos_guadalupe:feat_map')