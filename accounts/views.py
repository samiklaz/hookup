from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    print(request.user)
    print('yes')
    return render(request, 'account/index.html')



def user_login(request):
    return render(request, 'account/login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        birthday = request.POST.get('birthday', '')
        gender = request.POST.get('gender', '')
        password = request.POST.get('password', '')
        confirm_pass = request.POST.get('password_repeat', '')
        user_check = User.objects.filter(username=username)

        if user_check:
            messages.error(request, "Username already taken")
            return render(request, 'account/signup.html')

        if "%" in first_name or "%" in last_name or '%' in username or "&" in first_name or "&" in last_name or "&" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        elif "!" in first_name or "!" in last_name or '!' in username or "#" in first_name or "#" in last_name or "#" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        elif "$" in first_name or "$" in last_name or '$' in username or "^" in first_name or "^" in last_name or "^" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        elif "*" in first_name or "*" in last_name or '*' in username or "(" in first_name or "(" in last_name or "(" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        elif ")" in first_name or ")" in last_name or ')' in username or "+" in first_name or "+" in last_name or "+" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        elif "=" in first_name or "=" in last_name or '=' in username or "|" in first_name or "|" in last_name or "|" in username:
            messages.error(request, "Invalid input")
            return redirect('/account/signup/')

        if password == confirm_pass:
            print(first_name)
            print(last_name)
            print(username)
            print(email)
            print(phone_number)
            print(birthday)
            print(gender)
            print(password)


    else:
        return render(request, 'account/signup.html')

    return redirect('/')


def user_logout(request):
    return None


