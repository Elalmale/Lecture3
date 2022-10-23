from django.shortcuts import render
from datetime import datetime

def basic(request):
    ahora=datetime.now()
    dia=ahora.day
    mes=ahora.month
    decision=dia==23 and mes==10
    return render(request,"newyear/index2.html", {"variable1":dia,"variable2":mes,"variable3":decision} )