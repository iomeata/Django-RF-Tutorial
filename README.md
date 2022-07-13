# Django-RF-Docs-Tutorial

Django-RF-Docs-Tutorial By Ifeanyi Omeata

## Tutorial

---

### [1-INTRODUCTION](#)

---

<details>
  <summary>OPEN</summary>
<hr>

<details>
  <summary>1. Django RF Docs</summary>

### [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

</details>

<details>
  <summary>2. Create a virtual environment Venv</summary>

```python
  python -m venv venv
  source venv/bin/activate

  python -m venv venv
  Set-ExecutionPolicy Unrestricted -Scope Process
  source venv\Scripts\activate
```

</details>

<details>
  <summary>3. Install Django and Django REST framework</summary>

```python
  pip install django django-rest-framework django-shortcuts
```

```python
  pip freeze
```

```python
  pip install -r requirements.txt
```

```python
  pip freeze > requirements.txt
```

</details>

<details>
  <summary>4. Set up new project (tutorial) and app (quickstart)</summary>

```python
  django-admin startproject tutorial .
```

```python
  django-admin startapp quickstart
```

</details>

<details>
  <summary>5. Run Migrations</summary>

```python
  python manage.py makemigrations
```

```python
  python manage.py migrate
```

</details>

<details>
  <summary>6. Add Django Rest Framework and App to settings</summary>

[here](https://github.com/iomeata/Django-API-Tutorial-1/commit/388d9ef90e787e6836b472370251500993521611)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'quickstart',
]
```

</details>

<details>
  <summary>7. Create SuperUser</summary>

```python
python manage.py createsuperuser --email admin@example.com --username admin
```

</details>

<details>
  <summary>8. Create HyperlinkedModelSerializer for User and Group</summary>

[here](https://github.com/iomeata/Django-RF-Docs-Tutorial/commit/3705344a5098b551dab1d2586928d71e6783dbae)

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```

</details>

<details>
  <summary>9. Create Viewsets</summary>

[here](https://github.com/iomeata/Django-RF-Docs-Tutorial/commit/5ddefcfab2af982cc33ed7dabcaf97942bf0d470)

```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

</details>

<details>
  <summary>10. Create API Urls</summary>

[here](https://github.com/iomeata/Django-RF-Docs-Tutorial/commit/c70bc238d7d8824c56838132a946d84343df848e)

```python
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

</details>

<details>
  <summary>11. Set Pagination</summary>

[here](https://github.com/iomeata/Django-RF-Docs-Tutorial/commit/c0f58cb7b5ef664fa6ecca9b5dafd21efcf38b48)

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

or for a single ModelViewSet:

```python
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class FooViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
```

</details>

<details>
  <summary>12. Test Endpoints on Browsable API</summary>

```python
python manage.py runserver
```

```python
http://127.0.0.1:8000/groups/
```

![img.png](media/img.png)

```python
http://127.0.0.1:8000/users/
```

![img_1.png](media/img_1.png)

</details>

</details>

---

### [2-SERIALIZATION](#)

---

<details>
  <summary>1. Install pygments</summary>

```python
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
```

</details>

<details>
  <summary>2. Create new App "snippets"</summary>

```python
python manage.py startapp snippets
```

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]
```

</details>

<details>
  <summary>3. Create Snippets Model</summary>

```python
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```

```python
python manage.py makemigrations snippets
python manage.py migrate snippets
```

</details>

<details>
  <summary>4. Create SnippetSerializer</summary>

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```

</details>

<details>
  <summary>5. Understanding Serialization: Working with Django Shell</summary>

```python
python manage.py shell
```

Creating Model Objects

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()
```

Model Object --> Python Object (Serialization)

```python
serializer = SnippetSerializer(snippet)
serializer.data
```

```python
#{'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

Python Object --> JSON Object (Serialization) (Render from Python to JSON)

```python
content = JSONRenderer().render(serializer.data)
content
```

```python
#b'{"id":2,"title":"","code":"print(\\"hello, world\\")\\n","linenos":false,"language":"python","style":"friendly"}'
```

JSON Object --> Python Object (Deserialization) (Parse from JSON to Python)

```python
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
data
```

```python
#{'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

Python Object --> Model Object (Deserialization)

```python
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
```

Serializing Querysets

```python
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
```

```python
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```

</details>

<details>
  <summary>6. Using ModelSerializers</summary>

```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

Viewing Serializer Instance

```python
python manage.py shell
```

```python
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
```

```python
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```

</details>

<details>
  <summary>7. Using ModelSerializers</summary>

```python
python manage.py makemigrations snippets
python manage.py migrate snippets
```

</details>

<details>
  <summary>8. Using ModelSerializers</summary>

```python
python manage.py makemigrations snippets
python manage.py migrate snippets
```

</details>

---

### [3-DRF-PROJECT-IAMPYTHON](#)

---

<details>
  <summary>1. Django RF Docs</summary>

```python
https://www.django-rest-framework.org/
```

</details>

<details>
  <summary>2. Create-venv-DRF and Install Django</summary>

```python
python -m venv venv-DRF
source venv/bin/activate
```

```python
pip install django django-rest-framework django-shortcuts
```

</details>

<details>
  <summary>3. Add and Access REST framework's Default login and logout views</summary>

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

```python
python manage.py createsuperuser
```

```python
http://127.0.0.1:8000/api-auth/login/
```

![image3](/media/image3.png)

</details>

<details>
  <summary>4. Include DjangoModelPermissionsOrAnonReadOnly</summary>

```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

</details>

<details>
  <summary>5. Setup Demo for User Authentication in Urls</summary>

```python
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

```python
http://127.0.0.1:8000/
```

```python
http://127.0.0.1:8000/users/
```

```python
http://127.0.0.1:8000/users/1/
```

</details>

<details>
  <summary>6. Create PostgreSQL database</summary>

```python
# ubuntu command to access the postgres terminal
psql -d template1
# create postgres database
CREATE DATABASE mbd;
psql -h localhost
# create postgres database user
CREATE USER mcommerce WITH PASSWORD '123456';
# set user encoding to utf8
ALTER ROLE mcommerce SET client_encoding TO 'utf8';
# set user default_transaction_isolation
ALTER ROLE mcommerce SET default_transaction_isolation TO 'read committed';
# set user timezone
ALTER ROLE mcommerce SET timezone TO 'Africa/Lagos';
# for full text search - evaluate the similarity of two strings by the number of “trigrams” they share.
CREATE EXTENSION pg_trgm;
# search without worrying about accented characters, useful in different languages
CREATE EXTENSION unaccent;
# grant full access to the database
GRANT ALL PRIVILEGES ON DATABASE mbd TO mcommerce;
```

```python
pip install psycopg2
```

```python
ALLOWED_HOSTS = ['.example.com','127.0.0.1', 'localhost']
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdb',
        'USER': 'mcommerce',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

```python
python manage.py runserver
```

</details>

<details>
  <summary>7. Create Product App</summary>

```python
python manage.py startapp product
```

```python
INSTALLED_APPS = [
    ---
    'rest_framework',
    'product',
]
```

</details>

<details>
  <summary>8. Create Product Model</summary>

```python
from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

</details>

<details>
  <summary>9. Register Product Model in Admin</summary>

```python
from django.contrib import admin
from .models import Product


admin.site.register(Product)
```

```python
python manage.py runserver
```

</details>

<details>
  <summary>10. Create Productlist Serializer, URL and View</summary>

Type of Serializers

```python
- Simple Serializers
- Model Serializers
- HyperlinkedModel Serializers
- List Serializers
- Base Serializers
```

Serializer

```python
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
```

View

```python
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context)
```

tutorial/urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', include('product.urls')),
]
```

product/urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
]
```

```python
python manage.py runserver
```

```python
http://127.0.0.1:8000/products/productlist/
```

</details>

<details>
  <summary>11. Apply Authentication</summary>

```python
from .serializers import ProductSerializer
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context)
```

</details>

<details>
  <summary>12. Create Messagelist Serializer, URL and View</summary>

Serializer

```python
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
```

URL

```python
from django.urls import path
from . import views

urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
    path('messagelist/', views.list_messages, name='list-messages'),
]
```

View

```python
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from .serializers import ProductSerializer, MessageSerializer
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class Message():
    def __init__(self, email, content, created_at=None, updated_at=None):
        self.email = email
        self.content = content
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context)

@api_view(['GET', 'POST'])
def list_messages(request):
    message_obj = Message('customer@gmail.com', 'Hello People!')
    serializer = MessageSerializer(message_obj)
    context = {
        'data': serializer.data
    }
    return Response(context)
```

</details>

<details>
  <summary>13. Create ProductCategory Model</summary>

```python
from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.PositiveIntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name = models.ForeignKey('ProductCategory', related_name='ProductCategory',
                                      on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

</details>

<details>
  <summary>14. Add ProductCategory Model to Admin</summary>

```python
from django.contrib import admin
from .models import Product, ProductCategory


admin.site.register(Product)
admin.site.register(ProductCategory)
```

</details>

<details>
  <summary>15. Create Products Class Based Views</summary>

```python
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class Message():
    def __init__(self, email, content, created_at=None, updated_at=None):
        self.email = email
        self.content = content
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def list_messages(request):
    message_obj = Message('customer@gmail.com', 'Hello People!')
    serializer = MessageSerializer(message_obj)
    context = {
        'data': serializer.data
    }
    return Response(context, status=status.HTTP_200_OK)

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
            saved_data = serializer.save()
            context = {
                'data': serializer.data,
                'name': serializer.data.get('name'),
                'message': f"The product {saved_data.name} has been created."
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
                'data': serializer.data,
                'message': f"The product {name} has been updated."
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Product.objects.get(product_id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

</details>

<details>
  <summary>16. Mixins</summary>

ListModelMixin

```python
.list(request, *args, **kwargs) --> 200 OK
```

CreateModelMixin

```python
.create(request, *args, **kwargs) --> 201 Created --> 400 Bad Request
```

RetrieveModelMixin

```python
.retrieve(request, *args, **kwargs) --> 200 OK --> 404 Not Found
```

UpdateModelMixin

```python
.update(request, *args, **kwargs) --> 200 OK --> 400 Bad Request
.partial_update(request, *args, **kwargs) --> 200 OK --> 400 Bad Request
```

DestroyModelMixin

```python
.destroy(request, *args, **kwargs) --> 204 No Content --> 404 Not Found
```

</details>

<details>
  <summary>17. Create ListProductsMixins</summary>

URL

```python
from django.urls import path
from . import views
urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
    path('messagelist/', views.list_messages, name='list-messages'),
    path('classproductlist/', views.ListProducts.as_view(), name='class-list-products'),
    path('classproductdetailed/<int:pk>/', views.DetailedProducts.as_view(), name='class-detailed-products'),
    path('productlistmixins/', views.ListProductsMixins.as_view(), name='list-products-mixins'),
]
```

Views

```python
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class Message():
    def __init__(self, email, content, created_at=None, updated_at=None):
        self.email = email
        self.content = content
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    context = {
        'data': serializer.data
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def list_messages(request):
    message_obj = Message('customer@gmail.com', 'Hello People!')
    serializer = MessageSerializer(message_obj)
    context = {
        'data': serializer.data
    }
    return Response(context, status=status.HTTP_200_OK)

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
            saved_data = serializer.save()
            context = {
                'data': serializer.data,
                'name': serializer.data.get('name'),
                'message': f"The product {saved_data.name} has been created."
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
                'data': serializer.data,
                'message': f"The product {name} has been updated."
            }
            return Response(context, status=status.HTTP_200_OK)
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

```

</details>

<details>
  <summary>18. Create DetailedProductsMixins</summary>

URL

```python
from django.urls import path
from . import views


urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
    path('messagelist/', views.list_messages, name='list-messages'),
    path('classproductlist/', views.ListProducts.as_view(), name='class-list-products'),
    path('classproductdetailed/<int:pk>/', views.DetailedProducts.as_view(), name='class-detailed-products'),
    path('productlistmixins/', views.ListProductsMixins.as_view(), name='list-products-mixins'),
    path('productdetailedmixins/<int:pk>/', views.DetailedProductsMixins.as_view(), name='detailed-products-mixins'),
]
```

View

```python
---
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
```

</details>

<details>
  <summary>19. Install Django</summary>

```python
https://www.django-rest-framework.org/
```

</details>

<details>
  <summary>20. Install Django</summary>

```python
https://www.django-rest-framework.org/
```

</details>
