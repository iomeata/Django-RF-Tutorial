from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context)
