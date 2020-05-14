from django.db import models
from usuarios.models import User

class Publicacion(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(blank=True, auto_now=True)
    imagen = models.ImageField(upload_to='imgs/', max_length=350)

    def __str__(self):
        return self.nombre_usuario

class PublicacionBien(models.Model):
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imgs/', max_length=350)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pubs',
        blank=False,
        null=False,
    )
