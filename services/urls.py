from django.urls import path
from . import views
urlpatterns = [
path('', views.services, name="services"),
path('category/<int:category_id>', views.category, name='category'),
]