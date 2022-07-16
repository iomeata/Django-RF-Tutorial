from django.urls import path
from . import views


urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
    path('messagelist/', views.list_messages, name='list-messages'),
    path('classproductlist/', views.ListProducts.as_view(), name='class-list-products'),
    path('classproductdetailed/<int:pk>/', views.DetailedProducts.as_view(), name='class-detailed-products'),
    path('productlistmixins/', views.ListProductsMixins.as_view(), name='list-products-mixins'),
]
