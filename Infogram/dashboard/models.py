from django.db import models

class Publicacion(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(blank=True, auto_now=True)
    imagen = models.ImageField(upload_to='imgs/', max_length=350)

    def __str__(self):
        return self.nombre_usuario


