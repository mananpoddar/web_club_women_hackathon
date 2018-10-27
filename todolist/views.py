from django.shortcuts import render
from todolist.forms import input
from todolist.models import liste

def main_page(request):
    form = input()
    if request.method=="POST":
         form=input(request.POST)
         form.save()
         qs = liste.objects.all()#qs is the query set
         return render(request,"todolist/todolist.html",{"qs":qs,"form":form,})

        


    else:
          return render(request,"todolist/todolist.html",{"form":form,})
