from django.shortcuts import render
from django.views import View

#checar este
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class Register(View):
    def get(self, request):
        template_name = 'register.html'
        return render(request, template_name)

class LoginView(TemplateView):
    template_name = 'login.html'

