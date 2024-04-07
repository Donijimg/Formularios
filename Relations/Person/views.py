from django.shortcuts import render
from django.http import HttpResponse
from .models import Person,Dni
from .form import People


#formulario
def form(request):
  if request.method == "GET":
     form=People.objects.all()
     return render(request ,"signup_person.html",{
       'person': form
       })
  if request.method =="POST":
    form =People(request.POST)
    if form.is_valid:
      Person.objects.create(
         first_name=request.POST['first_name'],
         last_name=request.POST['last_name'],
         date=request.POST['date'],
         email=request.POST['email'],
         dni=request.POST['dni']
         )
    else:
      return render (request,'signup_person.html',{
        'person': form
      })
#guardar datos registrados
















#eliminar datos registrados
def funcion(request):
    objecto = request.GET['id']
    obejtoid=tabla.objects.get(id=obejtoid).delete()
    save_poblacion(objecto)
    return render(request, 'eliminar_poblacion.html', {'poblacion': poblacion})




#editar datos registrados
def editar_poblacion(request, poblacion_id):
    poblacion = Poblacion.objects.get(id=poblacion_id)
    if request.method == 'POST':
        nombre_poblacion = request.POST['nombre_poblacion']
        poblacion.nombre_poblacion = nombre_poblacion
        save_poblacion(poblacion)
        return HttpResponse(f"Se actualizó la población {poblacion.nombre_poblacion}.")
    return render(request, 'editar_poblacion.html', {'poblacion': poblacion})



#recuperar datos
def recuperar_poblacion(request):
    poblacion_id = request.GET['id']
    poblacion = Poblacion.objects.get(id=poblacion_id)
    save_poblacion(poblacion)
    return render(request, 'recuperar_poblacion.html', {'poblacion': poblacion})
