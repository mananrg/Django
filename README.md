
## Installation

You can install Django with

```sh
$ conda install django
```

Or

```sh
$ pip install django
```

When you install Django,it actually also installs a command line tool called:
*django-admin*

Let's create our first project:
**django-admin startproject first_project**

first_project
    first_project
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manange.py
To run 
**python manage.py runserver**

Lets create an app
-A Django Project is a collection of applications and configurations that when combined       together will make up the full web application(your complete websitr running with Django)
-A Django Application is created to perform a particular functionality for your entire web application.For example you could have a registration app, a polling app, comments app etc.
-These Django Apps can be then plugged into other Django Projects, so you can reuse them!(Or use other people's)

```sh
python manage.py startapp first_app
```

## Databases with Django

-Django can do the process of migration with simple command
```sh
$ python mannage.py migrate
```

-Register the changes to your app shown with some generic "app1":
```sh
$ python manage.py makemigrations app1
```

-Migrate the database one more time
```sh
$ python manage.py migrate
```

In order to fully use thr database and the Admin, we will need to crreate a "superuser"

'''sh
$ python manage.py createsuperuser
'''

## Security

pip install bcrypt
pip install django[argon2]