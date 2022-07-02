# Django-RF-Docs-Tutorial

Django-RF-Docs-Tutorial By Ifeanyi Omeata

## Tutorial

---

### [1-INTRODUCTION](#)

---
<details>
  <summary>Click to expand COURSE!</summary>

### 1. Django RF Docs

### [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

### 2. Create a virtual environment

```python
  python -m venv venv
  source venv/bin/activate

  python -m venv venv
  Set-ExecutionPolicy Unrestricted -Scope Process
  venv\Scripts\activate
```

### 3. Install Django and Django REST framework

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

### 4. Set up a new project with a single application
```python
  django-admin startproject tutorial .
```
```python
  django-admin startapp quickstart
```

### 5. Sync your database for the first time
```python
  python manage.py makemigrations
```
```python
  python manage.py migrate
```

### 6. Add Django Rest Framework to settings - [here](https://github.com/iomeata/Django-API-Tutorial-1/commit/388d9ef90e787e6836b472370251500993521611)

</details>