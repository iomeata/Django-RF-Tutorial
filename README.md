# Django-RF-Tutorial

Django-RF-Tutorial By Ifeanyi Omeata

## Tutorial

---

### [0-DOCS](https://github.com/iomeata/Django-RF-Tutorial/blob/main/DOCS.md)

---

---

### [1-PYTHON](#)

---

<details>
  <summary>#1. Python Classes</summary>

######################################
######################################
######################################

<details>
  <summary>1. Simple Python Class</summary>

```python
class Person:
  pass

p1 = Person()
p2 = Person()

p1.name = "Bob"
p1.age = 30

p2.name = "Henry"
p2.age = 25

print(p1.name, p1.age) #Bob 30
print(p2.name, p2.age) #Henry 25

```

</details>

<details>
  <summary>2. Class Initializer</summary>

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Brad", 32)
p2 = Person("Tommy", 21)

print(p1.name, p1.age) #Brad 32
print(p2.name, p2.age) #Tommy 21

```

</details>

<details>
  <summary>3. Class Attributes</summary>

```python
class Person:
  email = "mymail@example.com"

  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Brad", 32)
p2 = Person("Tommy", 21)

print(p1.name, p1.age, p1.email) #Brad 32 mymail@example.com
print(p2.name, p2.age, p2.email) #Tommy 21 mymail@example.com
```

</details>

<details>
  <summary>4. Class Methods</summary>

```python
class Person:
  email = "mymail@example.com"

  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

  def print_info(self):
    print(f'My name is {self.name}, I am {self.age} years old, and my email is {self.email}.')

p1 = Person("Brad", 32, "brad@example.com")
p1.print_info()
#My name is Brad, I am 32 years old, and my email is brad@example.com.
```

</details>

<details>
  <summary>5. Class Inheritance</summary>

```python
class Person:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def full_info(self):
    print(f'Name is {self.name}, and Email is {self.email}.')

class Student(Person):
  pass

p1 = Student("Brad", "brad@example.com")
p1.full_info()
#Name is Brad, and Email is brad@example.com
```

</details>

<details>
  <summary>6. Super Function</summary>

```python
class Person:
  def __init__(self):
    print("This is from the Super class!")

class Student(Person):
  def __init__(self):
    # Person.__init__(self)
    super().__init__()
    print("This is from the Sub class.")

p1 = Student()
#This is from the Super class!
#This is from the Sub class.
```

</details>

</details>

<details>
  <summary>#2. Python Built-in Functions</summary>

######################################
######################################
######################################

<details>
  <summary>1. Get Built-in Details</summary>

```python
print(dir(__builtins__))
print(dir(abs))
```

</details>

<details>
  <summary>2. Breakpoint</summary>

```python
for i in range(10):
  print(f"i={i}")

  if i == 7:
    #import pdb; pdb.set_trace()
    breakpoint()

# i=0
# i=1
# i=2
# i=3
# i=4
# i=5
# i=6
# i=7
# > /home/runner/Python-LAB/main.py(4)<module>()
# -> for i in range(10):
# (Pdb) i
# 7
# (Pdb) continue/ step
# i=8
# i=9
```

</details>

<details>
  <summary>3. Abs</summary>

```python
mylist = [1,2,3,-1,-2,-3]
my_new_list = [abs(i) for i in mylist]

print(mylist)
print(my_new_list)
# [1, 2, 3, -1, -2, -3]
# [1, 2, 3, 1, 2, 3]
```

</details>

<details>
  <summary>4. All</summary>

```python
print(all("hey")) #True
print(all("")) #True
print(all([False, 0])) #False
print(all([False, 1])) #False
print(all([False, False])) #False
print(all([True, False])) #False
print(all([True, True])) #True
print(all([10, 1])) #True

listSame = [1, 1, 1]
listDiff = [1, 2, 3]

print(all([x == 1 for x in listSame])) #True
print(all([x == 10 for x in listSame])) #False
print(all([x == 1 for x in listDiff])) #False

```

</details>

<details>
  <summary>5. Any</summary>

```python
print(any([""])) #False
print(any(["", False, 0])) #False
print(any(["", False, 0, 11])) #True
print(any(["", False, 0, True])) #True
print(any("Hey")) #True

listSame = [1, 1, 1]
listDiff = [1, 2, 3]

print(any([x == 1 for x in listSame])) #True
print(any([x == 10 for x in listSame])) #False
print(any([x == 1 for x in listDiff])) #True

names = ["John", "Joe", "James"]

print(any([x == "Joe" for x in names])) #True
print(any([x == "Dave" for x in names])) #False
```

</details>

<details>
  <summary>6. Ascii</summary>

```python
print(ascii(1)) # '1'
print(ascii([])) # '[]'
print(ascii('encod??')) # 'encod\xe9'
print(ascii('????????????')) # '\u0420\u043e\u0441\u0441\u0438\u044f'
print(ascii(['encod??', '????????????'])) # '['encod\xe9', '\u0420\u043e\u0441\u0441\u0438\u044f']'
print(type(ascii(['encod??', '????????????']))) # <class 'str'>

```

</details>

<details>
  <summary>7. Binary</summary>

```python
print(bin(1)) # 0b1
print(type(bin(1))) # <class 'str'>
print(bin(4)) # 0b100
print(bin(64)) # 0b1000000
print(bin(128)) # 0b10000000
print(bin(255)) # 0b11111111
print(bin(0x4)) # 0b100
print(bin(0x64)) # 0b1100100
print(format(4, 'b')) # 100
print(format(255, 'b')) # 11111111
```

</details>

<details>
  <summary>8. Bool</summary>

```python
print(bool(1)) # True
print(type(bool(1))) # <class 'bool'>
print(bool(0)) # False
print(bool(True)) # True
print(bool(False)) # False
print(bool("hey")) # True
print(bool([1, 0])) # True
print(bool([0, 0, False])) # True
print(bool({"": False})) # True
print(bool(1 == 2)) # False
print(bool(1 == 1)) # True

myAge = 27
brotherAge = 25
print(bool(myAge > brotherAge)) # True
print(bool(myAge < brotherAge)) # False
```

</details>

<details>
  <summary>9. Bytes and Bytearray</summary>

```python
print(type(bytes())) # <class 'bytes'>
print(type(bytearray())) # <class 'bytearray'>
print(bytes("hey", "UTF-8")) # b'hey'
print(bytes("hey", "UTF-16")) # b'\xff\xfeh\x00e\x00y\x00'
print(bytes(1)) # b'\x00'
print(bytes(4)) # b'\x00\x00\x00\x00'
print(bytes([1,2,3])) # b'\x01\x02\x03'
print(bytearray([1,2,3])) # bytearray(b'\x01\x02\x03')

x = bytearray([1,2,3])
x.append(4)
print(x) # bytearray(b'\x01\x02\x03\x04')
x.reverse()
print(x) # bytearray(b'\x04\x03\x02\x01')

print(bytearray("hey", "UTF-8", "strict")) # bytearray(b'hey')
print(bytearray("Po??c????", "UTF-8", "strict")) # bytearray(b'Po\xd1\x81c\xd0\xb8\xd1\x8f')
print(bytearray("Po??c????", "ascii", "ignore")) # bytearray(b'Poc')
print(bytearray("Po??c????", "ascii", "replace")) # bytearray(b'Po?c??')
```

</details>

<details>
  <summary>10. Callables</summary>

```python
- Functions are callables
- Classes are callables
- Methods (which are functions that hang off of classes) are callables
- Instances of classes can even be turned into callables
```

```python
x = "Hey"
y = type("Hey")
num = 5

def test_function():
  return "Hey"

class Example:
  def __init__(self):
    return 2 + 4

print(callable(x)) # False
print(callable(y)) # True
print(callable(num)) # False
print(callable(test_function)) # True
print(callable(Example)) # True
```

</details>

<details>
  <summary>11. Chr and Ord</summary>

```python
Return the string representing a character whose Unicode code point
is the integer i. For example, chr(97) returns the string 'a', while
chr (8364) returns the string 'e'. This is the inverse of ord().
```

```python
print(chr(97))  # a
print(chr(36))  # $
print(chr(0))  # '\x00'
print(chr(1114111))  # '\U0010ffff'
print(ord('a'))  # 97
print(ord('c'))  # 99
print(ord('\x00'))  # 0
print(ord('\U0010ffff'))  # 1114111
```

</details>

<details>
  <summary>12. @classmethod decorator</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

<details>
  <summary>80. Serializers</summary>

```python

```

</details>

</details>

---

### [2-DRF-DOCS](#)

---

<details>
  <summary>1. Django RF Official Docs</summary>

### [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

</details>

<details>
  <summary>2. Create a virtual environment Venv</summary>

```python
  python -m venv venv
  source venv/bin/activate

  python -m venv venv
  #Set-ExecutionPolicy Unrestricted -Scope Process
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
  <summary>4. Create new project (tutorial) and app (quickstart)</summary>

```python
  django-admin startproject tutorial .
```

```python
  django-admin startapp quickstart
```

```python
  python manage.py makemigrations
```

```python
  python manage.py migrate
```

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
  <summary>5. Create SuperUser</summary>

```python
python manage.py createsuperuser --email admin@example.com --username admin
```

</details>

<details>
  <summary>6. Create HyperlinkedModelSerializer(User and Group)/Viewsets/API URLs</summary>

- HyperlinkedModelSerializer

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

- Viewsets

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

- API URLs

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
  <summary>7. Set Pagination</summary>

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
  <summary>8. Test Endpoints on Browsable API</summary>

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

<details>
  <summary>9. Install pygments module/Create new App snippets</summary>

```python
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
```

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
  <summary>10. Create Snippets Model/SnippetSerializer</summary>

- Snippets Model

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

- SnippetSerializer

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
  <summary>11. Understanding Serialization: Working with Django Shell</summary>

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
  <summary>12. Using ModelSerializers</summary>

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
  <summary>13.</summary>

```python

```

</details>

<details>
  <summary>14.</summary>

```python

```

</details>

---

### [2-DRF-PROJECT-IAMPYTHON](#)

---

<details>
  <summary>1. Django RF Official Docs</summary>

### [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

</details>

<details>
  <summary>2. Create a virtual environment Venv</summary>

```python
  python -m venv venv
  source venv/bin/activate

  python -m venv venv
  #Set-ExecutionPolicy Unrestricted -Scope Process
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
  <summary>4. Add REST framework's Default login and logout views</summary>

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
  <summary>5. Include DjangoModelPermissionsOrAnonReadOnly</summary>

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
  <summary>6. Setup User Authentication in Urls</summary>

```python
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'password']
        read_only_fields = ('is_active', 'is_superuser', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data, is_active=True, is_staff=True, is_superuser=True)

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
  <summary>7. Create PostgreSQL database</summary>

```python
# ubuntu command to access the postgres terminal
psql -d template1
# create postgres database
CREATE DATABASE mbd;
#psql -h localhost
# create postgres database user
CREATE USER mcommerce WITH PASSWORD '123456';
# set user encoding to utf8
ALTER ROLE mcommerce SET client_encoding TO 'utf8';
# set user default_transaction_isolation
ALTER ROLE mcommerce SET default_transaction_isolation TO 'read committed';
# set user timezone
ALTER ROLE mcommerce SET timezone TO 'Africa/Lagos';
# for full text search - evaluate the similarity of two strings by the number of ???trigrams??? they share.
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
        'NAME': 'mbd',
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
  <summary>8. Create Product App and Product Model</summary>

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

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-product_id",)
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

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
  <summary>9. Create Productlist Serializer, URL and View</summary>

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
  <summary>10A. View Snippets</summary>

drf-1

```python
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import Driver, Car
from .serializers import DriverSerializer, CarSerializer


# class DriverListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

# class DriverUpdateAPIView(generics.UpdateAPIView):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer
#     lookup_field = "id"

# class CarListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarUpdateAPIView(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     lookup_field = "id"


def get(self, request):
    query_cars = Car.objects.all()
    context = {
        "drivers": DriverSerializer(query_drivers, many=True).data,
        "cars": CarSerializer(query_cars, many=True).data
    }
    return Response(context)

def post(self, request):
    if request.data.get('object') == "driver":
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    elif request.data.get('object') == "car":
        driver = Driver.objects.get(username=request.data.get('driver'))
        serializer = CarSerializer(data=request.data)
        serializer.is_valid()
        Car.objects.create(
            driver_id=driver,
            **serializer.data
        )
    context = {"data": serializer.data}
    return Response(context)

def put(self, request, *args, **kwargs):
    model_id = kwargs.get("id", None)
    if not model_id:
        return Response({"error": "method /PUT/ not allowed. No id exists."})
    try:
        instance = Driver.objects.get(id=model_id)
    except Exception:
        return Response({"error": "Object does not exist."})

    serializer = DriverSerializer(data=request.data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"data": serializer.data})


def delete(self, request):
    driver = Driver.objects.get(username=request.data.get('driver'))
    driver.delete()
    context = {"data": request.data}
    return Response(context)

```

drf-2

```python
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from functools import wraps
from .models import Customer
from .serializers import CustomerSerializer


class CustomerAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        customers = Customer.published.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def resource_checker(model):
    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({'error': 'Resource Not Found'}, status=status.HTTP_204_NO_CONTENT)
        return inner_fun
    return check_entity


class CustomerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @resource_checker(Customer)
    def get(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @resource_checker(Customer)
    def put(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @resource_checker(Customer)
    def delete(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

drf-3

```python
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import random
import string
import datetime
import jwt

from .serializers import UserSerializer
from .models import User, UserToken, Reset
from .authentication import (JWTAuthentication, create_access_token,
                             create_refresh_token, decode_refresh_token)


class MembersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data.get('password') != data.get('password_confirm'):
            raise exceptions.APIException('Passwords do not match!')
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User is Registered!', 'data': serializer.data})

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id = user.id,
            token = refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }
        return response

class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


def post(request):
    refresh_token = request.COOKIES.get('refresh_token')
    id = decode_refresh_token(refresh_token)

    if not UserToken.objects.filter(
        user_id=id,
        token=refresh_token,
        expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
    ).exists():
        raise exceptions.AuthenticationFailed('unauthenticated')

    access_token = create_access_token(id)
    return Response({
        'token': access_token
    })


class RefreshAPIView(APIView):
    pass

class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'successfully logged out'
        }
        return response

class ForgotAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        token = jwt.encode({"email": email}, "secret", algorithm="HS256")
        otp = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        # otp = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        # otp = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))
        if Reset.objects.filter(email=email).exists():
            Reset.objects.filter(email=email).delete()

        Reset.objects.create(
            email=email,
            otp=otp,
            token=token
        )

        url = f'http://localhost:3000/reset/{token}'
        url_otp = 'http://localhost:3000/reset/'

        send_mail(
            subject='Reset your Password!',
            message=f"""
                    Hi,
                    Click {url} to reset your password!
                    OR
                    Click the link below to reset your Password with the OTP: {otp}.
                    {url_otp}

                    Regards,
                    example.com
                    """,
            from_email = 'from@example.com',
            recipient_list = [email],
            fail_silently=False,
        )

        return Response({
            'message': 'successfully sent pin to email.'
        })


class ResetAPIView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('passwords do not match!')

        reset_password = Reset.objects.filter(otp=data['otp']).first()
        if not reset_password:
            raise exceptions.APIException('Invalid link')

        user = User.objects.filter(email=reset_password.email).first()
        if not user:
            raise exceptions.APIException('User not found!')

        user.set_password(data['password'])
        user.save()

        return Response({
            'message': 'Password changed successfully!'
        })

```

Others

```python
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_assessment_count(request):
    [...]
    data = {'count': queryset.count()}
    return Response(data, template_name='assessments.html')

```

</details>

<details>
  <summary>11. Apply Authentication</summary>

```python
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


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
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
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

```

</details>

<details>
  <summary>13. Create ProductCategory Model</summary>

```python
from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField(primary_key=True)
    category_name = models.ForeignKey('ProductCategory', related_name='ProductCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-product_id",)


class ProductCategory(models.Model):
    category_id = models.PositiveIntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ("-category_id",)
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

```python
from django.contrib import admin
from .models import Product, ProductCategory


admin.site.register(Product)
admin.site.register(ProductCategory)
```

</details>

<details>
  <summary>14. Create Products Class Based Views</summary>

View:

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

```

URL:

```python
from django.urls import path
from . import views


urlpatterns = [
    path('productlist/', views.list_products, name='list-products'),
    path('messagelist/', views.list_messages, name='list-messages'),
    path('classproductlist/', views.ListProducts.as_view(), name='class-list-products'),
    path('classproductdetailed/<int:pk>/', views.DetailedProducts.as_view(), name='class-detailed-products'),
]

```

</details>

<details>
  <summary>15. Mixins</summary>

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
  <summary>16. Create ListProductsMixins</summary>

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
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

------

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
  <summary>17. Create DetailedProductsMixins</summary>

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
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


-----

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

```

</details>

<details>
  <summary>18. </summary>

```python

```

</details>

<details>
  <summary>19. </summary>

```python

```

</details>
