# Django-RF-Docs-Tutorial

Django-RF-Docs-Tutorial By Ifeanyi Omeata

## Tutorial

---

### [1-INTRODUCTION](#)

---

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
  <summary>#. Create a virtual environment</summary>

</details>



