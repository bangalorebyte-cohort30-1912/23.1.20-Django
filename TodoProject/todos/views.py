from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from todos.models import Todo

TODOS = [{'id': 1,
          'text': 'django-admin startproject TodoApplication',
          'iscomplete': True
          },
         {'id': 2,
          'text': 'python manage.py runserver',
          'iscomplete': True
          },
         {'id': 3,
          'text': 'python manage.py migrate ',
          'iscomplete': True
          },
         {'id': 4,
          'text': 'python manage.py createsuperuser',
          'iscomplete': False
          },
         {'id': 5,
          'text': 'python manage.py startapp todos ',
          'iscomplete': True
          },
         {'id': 6,
          'text': '// add application to INSTALLED_APPS',
          'iscomplete': True
          },
         {'id': 7,
          'text': '// added bootstrap and fontawesome in templates',
          'iscomplete': False
          }]

class TodoView(View):
    template_name = 'todos/index.html'

    def get(self, request, *args, **kwargs):
        
        context = {
            'todos': Todo.objects.all()
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        todotext = request.POST['todotext']
        obj = Todo(todo_text=todotext)
        obj.save()
        context = {
            'todos': Todo.objects.all()
        }
        return render(request, self.template_name, context)

    

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         context = {
#         'todos' : TODOS
#         }
#         print(request.method)
#         return render(request, 'todos/index.html', context=context)
#     elif request.method == "POST":

#         try:
#             todotext = request.POST['todotext']
#         except:
#             todotext= "unable to capture form data"
#         TODOS.append({
#             'id' : len(TODOS)+1,
#             'text': todotext,
#             'iscomplete':False
#             })
#         context = {
#             'todos': TODOS
#             }
#         return render(request, 'todos/index.html', context)


