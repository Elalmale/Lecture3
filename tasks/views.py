from django.shortcuts import render

tasks=["correr","caminar","nadar"]

# Create your views here.

def lista(request):
    return render(request,"tasks/plantillalista.html",{"lista":tasks})

def add(request):
    return render(request,"tasks/add.html")