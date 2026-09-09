from django.urls import path
from . import views

app_name = 'app_deportivos_guadalupe'

urlpatterns = [
    # Accesible en: http://127.0.0.1:8000/guadalupe/garaje/
    path('garaje/', views.garaje_view, name='garaje'),
]