from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def HomeView(request):
    return HttpResponse("<h1>Hello World</h1>")


def AboutUsView(request):
    return HttpResponse("<h1>About Us</h1>")


def ContactUsView(request):
    return HttpResponse("<h1>Contact Us</h1>")
