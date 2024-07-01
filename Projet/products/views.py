from django.shortcuts import render
from django.http import HttpResponse

def index(request, *args, **kargs):
    text = "Je suis django dans le views"
    return HttpResponse(text)
