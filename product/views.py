from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_products(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        context = {
            'data': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
