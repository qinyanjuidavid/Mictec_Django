from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def Homeview(request):
    return HttpResponse("Hello world")
def contacts(request):
  return HttpResponse("011029297"),
def AboutUs(request):
  return HttpResponse("location"),
