1. make sure python3 and pip3 are installed
```
 python3 --version
 pip3 --version
```

2. install `pipenv`
```
pip3 install pipenv
```
3. create a virtual directory
```
pipenv shell
```
4. install `django`, `django-rest-frame-work`
```
pipenv install django djangorestframework
```

5. start a new django project
```
django-admin startproject <project_name>
```
6. start a new app
```
python3 manage.py startapp <app_name>
```

7. migrations - 
```
python manage.py makemigrations <app_name>
python manage.py migrate
```
8. run app -
```
python manage.py runserver
```

