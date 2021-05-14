from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def demoPage(request):
    return HttpResponse("demo page")


def demoPageTemplate(request):
    return render(request, "demo.html")


def adminLogin(request):
    return render(request, "admin_templates/login.html")


def admin_login_process(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request=request, username=username,password=password)

    if user is not None:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request, "Login Error! Invalid credentials!")
        return HttpResponseRedirect(reverse("admin_login"))


def admin_logout_process(request):
    logout(request)
    messages.success(request, "Successful logout!")
    return HttpResponseRedirect(reverse("admin_login"))
