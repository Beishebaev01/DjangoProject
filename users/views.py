from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'users/register.html', context={'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data.__delitem__('password_confirm')
            user = User.objects.create_user(**form.cleaned_data)
            return redirect("/")
        else:
            return render(request, 'users/register.html', context={'form': form})


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'users/login.html', context={'form': form})
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")
                return render(request, 'users/login.html', context={'form': form})
        else:
            return render(request, 'users/login.html', context={'form': form})
        

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect("/")