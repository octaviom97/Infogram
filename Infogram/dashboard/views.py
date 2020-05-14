from django.shortcuts import render, redirect
from django.views import View
from .models import PublicacionBien
from .forms import PublicacionForm
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        template_name = 'index.html'
        contexto = dict(pubs=PublicacionBien.objects.all())
        return render(request, template_name, contexto)

class PerfilView(View):
    def get(self, request):
        template_name = 'index.html'
        user = request.user
        contexto = dict(pubs=PublicacionBien.objects.filter(user=user))
        return render(request, template_name, contexto)

class PublicacionCreate(View):
    template_name = 'crear_pub.html'

    def get(self, request):
        contexto = dict(form=PublicacionForm(initial={'user': request.user}))
        return render(request, self.template_name, contexto)

    def post(self, request):
        data = request.POST
        form = PublicacionForm(data, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hiciste una publicación')
            return redirect('perfil')
        else:
            messages.error(request, 'No se guardó la publicación')
            return redirect('pub-crear')

class NotificacionCreate(View):
    template_name = 'notification.html'



