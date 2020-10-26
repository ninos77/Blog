from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_v(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = form.save()
        login(request, user)
        return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def logout_v(request):
    logout(request)
    return redirect('home')
