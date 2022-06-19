# Django Dashboard

This is a draft Django dashboard app for shared platform to test and control trading models. The layout is based on the template of the [Black Django Dashboard](https://github.com/app-generator/django-black-dashboard).

## How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/kjanker/django-dashboard.git
$ cd django-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

