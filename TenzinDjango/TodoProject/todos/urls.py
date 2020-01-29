from django.urls import path
from django.conf.urls import include, url

from .views import TodoView

urlpatterns = [
    path('', TodoView.as_view(), name="todos-index"),
]
