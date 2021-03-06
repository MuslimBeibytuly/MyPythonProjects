import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main_app.models import Code

def auth_view(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "registration/auth.html")

def reg_view(request):
    if (request.method == "POST"):
        print("Got in")
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if re.match(r'^[A-Za-z\d]{6,}$', password) and password == repassword:
            if User.objects.filter(username=email).exists():
                return render(request, "registration/reg.html")
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.is_active = False
                user.save()

                newCodes = Codes()
                newCodes.user = user
                newCodes.save()

                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect('/profile')
        else:
            return render(request, "registration/reg.html")
    else:
        return render(request, "registration/reg.html")

def logout_view(request):
    logout(request)
    return redirect('index')
