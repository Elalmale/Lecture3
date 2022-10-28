from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse




class formumulario(forms.Form):
    task=forms.CharField(label="Nueva actividad")
    #prioridad=forms.IntegerField(label="prioridad", min_value=0,max_value=5)

# Create your views here.

def lista(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"tasks/plantillalista.html",{"lista":request.session["tasks"]})

def add(request):
    if request.method=="POST":
        form=formumulario(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:lista"))
        else:
            return render(request,'tasks/add.html',{"form":form} )


    return render(request,"tasks/add.html", {"form":formumulario()})