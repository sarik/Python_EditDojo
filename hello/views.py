from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse('<i>On Hello World Page.Thanks</i>')
