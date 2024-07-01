from django.shortcuts import render
from . models import Articles
from . form import ArticleForm


def index(request, *args, **kargs):
   article = Articles.objects.all()

   context = {
      'articles': article
   }
   return render(request, 'product/index.html', context)


def addAticle(request):
   messages = ""
   form = ArticleForm(request.POST or None, request.FILES or None)
   if request.method == 'POST' and form.is_valid():
         form.save()
         form = ArticleForm()
         messages = "We have successfuly add an item"
   return render(request, 'product/add.html', {'form': form, 'message': messages})


def table(request):
    article = Articles.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'product/table.html', context)


def modifier(request, pk):
    obj = Articles.objects.get(id=pk)
    messages =""
    form = ArticleForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ArticleForm()
        messages = "We have successfuly modified thank"
    return render(request, 'product/modifier.html', {'form': form, 'message': messages})