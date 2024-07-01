from django.shortcuts import render
from . models import Articles


def index(request, *args, **kargs):
   article = Articles.objects.all()

   context = {
      'articles': article
   }

   return render(request, 'product/index.html', context)
