from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, bnbvncpayaso")

def alvaro(request):
    return HttpResponse("Hoy va a ser un gran dia")

def pepe(request):
    return HttpResponse("Hoy va a ser un gran dia o no")

def paratodos(request, plus):
    ahora=datetime.now()
    resultado = f"hoy es el dia {ahora.day}, mira que eres tonto {plus.capitalize()}"
    return render(request,"hello/plantilla.html",{"name":resultado})