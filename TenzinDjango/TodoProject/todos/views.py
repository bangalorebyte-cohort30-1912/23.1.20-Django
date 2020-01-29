from django.shortcuts import render, get_object_or_404, redirect
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
        # id = request.POST['id']
        # text = request.POST['text']
        data = request.POST
        print(data['id'], data['text'])
        Todo.objects.filter(id=data['id']).update(todo_text=data['text'])
        
        
        context = { 
            'todos': Todo.objects.all()
        }


        return render(request, self.template_name, context)

# class ToUpdateView(View):
#     template_name = 'todos/index.html'

#     def update(self, request, *args, **kwargs) :
#             ola = request.POST['ola']
#             context = {
#                'todos': Todo.objects.filter(id= ola).update(to_dotext='Plice man'),
#                'todos': Todo.objects.all()
#                 } 
#             return render(request, self.template_name, context)   

    

       

