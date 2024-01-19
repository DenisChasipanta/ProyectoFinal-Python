from django.shortcuts import render, get_object_or_404
from .models import Category,Service

# Create your views here.
def services(request):
    services= Service.objects.all()
    return render(request, 'services/services.html',{'services':services})

def category(request,category_id):
    # conocer la categoria a trabajar
    # category = Category.objects.get(id = category_id)
    category= get_object_or_404(Category, id=category_id)
    # filtrando los blogs por la categoria trabajada
    Service = Service.objects.filter(category=category) #el primer nombre es el que tengo en el modelo y el otro el que esta en esta vista - lista de blogs
    return render(request, 'service/category.html', {'category':category})

