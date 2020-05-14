from django.contrib import admin
from .models import Publicacion, PublicacionBien


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_usuario', 'descripcion', 'fecha_publicacion']

@admin.register(PublicacionBien)
class PublicacionBienAdmin(admin.ModelAdmin):
    list_display = ['user', 'descripcion', 'fecha_publicacion']