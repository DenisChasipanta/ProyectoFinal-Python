from django.shortcuts import render, get_object_or_404
from .models import Category,Testimonial

# Create your views here.
def testimonials(request):
    testimonials= Testimonial.objects.all()
    return render(request, 'testimonials/testimonial.html',{'testimonials':testimonials})

def category(request,category_id):
    # conocer la categoria a trabajar
    # category = Category.objects.get(id = category_id)
    category= get_object_or_404(Category, id=category_id)
    # filtrando los blogs por la categoria trabajada
    Testimonial= Testimonial.objects.filter(category=category) #el primer nombre es el que tengo en el modelo y el otro el que esta en esta vista - lista de blogs
    return render(request, 'testimonials/category.html', {'category':category})


