from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def HomeView(request):
    return HttpResponse("<h1>Hello World</h1>")
