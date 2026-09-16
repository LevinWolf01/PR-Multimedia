from django.urls import path
from . import views

app_name = 'app_deportivos_guadalupe'

urlpatterns = [
    # Accesible en: http://127.0.0.1:8000/guadalupe/garaje/
    path('garaje/', views.garaje_view, name='garaje'),

    path('feat-map/', views.mapa_view, name='feat_map'),
    path('feat-map/api/ubicaciones/', views.ubicaciones_api, name='ubicaciones_api'),
    path('feat-map/api/ubicaciones/<int:ubicacion_id>/', views.ubicacion_api, name='ubicacion_api'),
    path('feat-map/api/rutas/', views.trayectorias_api, name='rutas_api'),
    path('feat-map/api/rutas/<int:trayectoria_id>/', views.trayectoria_api, name='ruta_api'),
    path('feat-SoliAdds/', views.solicitudes_adicion_view, name='feat_soliadds'),
    path('features_test/', views.evacuacion, name='features_test'),
]