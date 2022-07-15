from django.urls import path
from . import views


urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
]
