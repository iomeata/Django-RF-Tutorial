from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
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
        if serializer.is_valid(raise_exception=True):
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
        if serializer.is_valid(raise_exception=True):
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProducts(APIView):
    def get(self, request):
        try:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            context = {
                'data': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            context = {
                'message': 'No products found.'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = serializer.data.get('name')
            context = {
                'message': f"The product {name} has been created.",
                'data': serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailedProducts(APIView):
    def get(self, request, pk):
        try:
            queryset = Product.objects.get(product_id=pk)
            serializer = ProductSerializer(queryset)
            context = {
                'data': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        queryset = Product.objects.get(product_id=pk)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = serializer.data.get('name')
            context = {
                'message': f"The product {name} has been updated.",
                'data': serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Product.objects.get(product_id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListProductsMixins(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailedProductsMixins(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)