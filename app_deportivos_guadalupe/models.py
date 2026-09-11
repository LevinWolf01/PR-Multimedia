from django.db import models

# Create your models here.
class Reporte(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField()
    #Cada tipo de arhivo va a su subcarpeta dentro de 'media/'
    foto        = models.ImageField(upload_to='reports/images/')
    documento   = models.FileField(upload_to='reports/docs/')
    audio       = models.FileField(upload_to='reports/audios/')
    video       = models.FileField(upload_to='reports/videos/')
    fecha       = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre