from django.http import HttpResponse
from django.shortcuts import render
from .form import Contact

def form(request):
  if request.method == "GET":
     form=Contact()
     return render(request ,"formulario.html",{
       'formularios': form
       })
  if request.method =="POST":
    form =Contact(request.POST)
    if form.is_valid:
      return HttpResponse("Formulario por post")
    else:
      return render (request,'formulario.html',{
        'formularios': form
      })
