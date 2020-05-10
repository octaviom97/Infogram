from django.shortcuts import render
from django.views import View

class BaseView(View):
    def get(self, request):
        template_name = 'base.html'
        return render(request, template_name)
