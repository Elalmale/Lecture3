from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path("alvar",views.alvaro, name="alvaro"),
    path("pepe",views.pepe, name="pepe"),
    path("<str:plus>",views.paratodos, name="ret")
    ]