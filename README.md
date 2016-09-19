# todo-api

## setup ##
- Install virtualenv
- source djangodev/bin/activate
- pip install requirements.txt
- cd todoapp
- python manage.py createsuperuser
- python manage.py runserver
- Open browser and hit 127.0.0.1:8000/todos/
- You can execute this too `curl -H 'Accept: application/json; indent=4' -u admin:1234 http://127.0.0.1:8000/todos/`

## test ##
- cd todoapp
- python manage.py test todos
