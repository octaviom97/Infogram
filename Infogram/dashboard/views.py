from django.shortcuts import render
from django.views import View
from .models import Publicacion

class IndexView(View):
    def get(self, request):
        template_name = 'index.html'
        contexto = dict(pubs=Publicacion.objects.all())
        return render(request, template_name, contexto)


