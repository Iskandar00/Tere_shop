from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.forms import BaseModelForm
from django.shortcuts import redirect, render
from apps.users.forms import UserCreateForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class UserRegisterView(TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        form = UserCreateForm({'username': username, 'password': password, 'first_name': first_name})
        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            messages.error(request, form.errors)

        return redirect('register')


class UserLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home-page')
        return super().get(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
