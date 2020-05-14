from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = LoginForm()
            return render(request, self.template_name, dict(form=form))

    def post(self, request):
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Autenticación exitosa')
            return redirect('index')
        messages.error(request, 'Los datos ingresados no son los correctos')
        return redirect('login')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, dict(form=form))

    def post(self, request):
        data = request.POST
        form = RegisterForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect('index')
        else:
            messages.error(request, 'Algo salió mal con tu registro, intentalo otra vez')
            return render(request, self.template_name, dict(form=form))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
