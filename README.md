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
  <summary>2. Create a virtual environment</summary>

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
  <summary>4. Set up a new project with a single application</summary>

```python
  django-admin startproject tutorial .
```
```python
  django-admin startapp quickstart
```

</details>

<details>
  <summary>5. Sync your database for the first time</summary>

```python
  python manage.py makemigrations
```
```python
  python manage.py migrate
```

</details>

<details>
  <summary>6. Add Django Rest Framework to settings</summary>

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
]
```

</details>

<details>
  <summary>#. Create a virtual environment</summary>

</details>
