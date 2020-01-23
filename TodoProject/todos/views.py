from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'todos' :[{   'id':1,
                    'text': 'django-admin startproject TodoApplication',
                    'iscomplete': True
                },
                {   'id': 2,
                    'text': 'python manage.py runserver',
                    'iscomplete': True
                },
                {   'id': 3,
                    'text': 'python manage.py migrate ',
                    'iscomplete': True
                },
                {   'id': 4,
                    'text': 'python manage.py createsuperuser',
                    'iscomplete': True
                },
                {   'id': 5,
                    'text': 'python manage.py startapp todos ',
                    'iscomplete': True
                },
                {   'id': 6,
                    'text': '// add application to INSTALLED_APPS',
                    'iscomplete': True
                }]
            }
    return render(request, 'todos/index.html', context=context)
