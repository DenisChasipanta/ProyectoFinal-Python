from django.shortcuts import render
from .models import Articulo

# Create your views here.
def articles(request):
    articles = Articulo.objects.all()
    return render(request, 'articulos/articles.html',{'articles':articles})