from django.shortcuts import render


def index(request, *args, **kargs):

   return render(request, 'product/index.html')
