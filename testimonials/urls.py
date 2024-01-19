from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials, name="testimonial"),
    path('category/<int:category_id>', views.category, name='category'),
]