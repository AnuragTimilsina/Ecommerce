from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def demoPage(request):
    return HttpResponse("demo page")


def demoPageTemplate(request):
    return render(request, "demo.html")


def adminLogin(request):
    return render(request, "admin_templates/login.html")

