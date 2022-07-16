from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
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


class Message():
    def __init__(self, email, content, created_at=None, updated_at=None):
        self.email = email
        self.content = content
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()


@api_view(['GET', 'POST'])
def list_messages(request):
    if request.method == 'GET':
        message_obj = Message('customer@gmail.com', 'Hello People!')
        serializer = MessageSerializer(message_obj)
        context = {
            'data': serializer.data
        }
        return Response(context)

    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
