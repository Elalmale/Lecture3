from django.urls import path
from . import views

app_name="tasks"
urlpatterns=[
    path("",views.lista,name="lista"),
    path("add",views.add,name="añadir")
]