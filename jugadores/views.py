from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from jugadores import models


def home(request):
	return render(request, 'general/index.html')

def posicion(request, id):
	objeto = models.Posicion.objects.get(id=id)
	if request.method == "POST":
		objeto.delete()
		return HttpResponseRedirect('/posicion/listado')
	plantilla = 'posicion/posicion.html'
	return render(request, plantilla, {'objeto':objeto})

def posicion_editar(request, id):
	mensaje = ''
	objeto = models.Posicion.objects.get(id=id)
	if request.method == "POST":
		if request.POST.get('nombre', ''):
			nombre = request.POST['nombre'].upper()
			if objeto.nombre != nombre:
				editar = True
				try:
					objeto = models.Posicion.objects.get(nombre=nombre)
					mensaje = "Ya existe posicion con la información ingresada"
					editar = False
				except objeto.DoesNotExist:
					editar = True
				if editar:
					objeto = models.Posicion.objects.get(id=id)
					objeto.nombre = nombre
					objeto.save()
					mensaje = "Se ha modificado la información de la posicion"
		else:
			mensaje = "Debe ingresar el nombre de la posicion"
	plantilla = 'posicion/editar.html'
	return render(request, plantilla, {'objeto':objeto, 'mensaje':mensaje})

def posicion_nuevo(request):
	mensaje = ''
	if request.method == "POST":
		objeto = models.Posicion
		if request.POST.get('nombre', ''):
			nombre = request.POST['nombre'].upper()
			try:
				objeto = models.Posicion.objects.get(nombre=nombre)
				mensaje = "Ya existe posicion con la información ingresada"
			except objeto.DoesNotExist:
				objeto = objeto.objects.create_object(nombre)
				objeto.save()
				return HttpResponseRedirect('/posicion/listado')
		else:
			mensaje = "Debe ingresar el nombre de la posicion"
	plantilla = 'posicion/nuevo.html'
	return render(request, plantilla, {'mensaje':mensaje})

def posiciones(request):
	listado = models.Posicion.objects.all()
	plantilla = 'posicion/lista.html'
	return render(request, plantilla, {'listado':listado})


# jugadores

def jugador(request, id):
	objeto = models.Jugador.objects.get(id=id)
	if request.method == "POST":
		objeto.delete()
		return HttpResponseRedirect('/jugador/listado')
	posiciones = models.Posicion.objects.all()
	plantilla = 'jugador/jugador.html'
	return render(request, plantilla, {'objeto':objeto, 'posiciones':posiciones})

def jugador_editar(request, id):
	mensaje = ''
	objeto = models.Jugador.objects.get(id=id)
	if request.method == "POST":
		try:
			
			dorsal = ""
			nombre = ""
			apellido = ""
			posicion = models.Posicion

			if request.POST.get('dorsal', ''):
				dorsal = request.POST['dorsal'].upper()
				if request.POST.get('nombre', ''):
					nombre = request.POST['nombre'].upper()
					if request.POST.get('apellido', ''):
						apellido = request.POST['apellido'].upper()
						if request.POST.get('posicion', ''):
							posicion = posicion.objects.get(id=int(request.POST['posicion']))
							if objeto.posicion.id != posicion.id or objeto.dorsal != dorsal or objeto.nombre != nombre or objeto.apellido != apellido:
								editar = True
								print("Editar")
								if objeto.posicion.id != posicion.id and objeto.dorsal != dorsal and objeto.nombre != nombre:
									try:
										objeto = models.Jugador.objects.get(dorsal=dorsal, nombre=nombre, apellido=apellido, posicion=posicion)
										mensaje = "Ya existe jugador con la información ingresada"
										editar = False
									except objeto.DoesNotExist:
										editar = True
								if editar:
									objeto = models.Jugador.objects.get(id=id)
									objeto.posicion = posicion
									objeto.dorsal = dorsal
									objeto.nombre = nombre
									objeto.apellido = apellido
									objeto.save()
									mensaje = "Se ha modificado la información del jugador"
						else:
							mensaje = "Debe seleccionar la posicion del jugador"
					else:
						mensaje = "Debe ingresar el apellido del jugador"
				else:
					mensaje = "Debe ingresar el nombre del jugador"
			else:
				mensaje = "Debe ingresar el dorsal del jugador"
			
		except posicion.DoesNotExist:
			mensaje = "La posicion seleccionada no existe"
		except objeto.DoesNotExist:
			objeto = models.Jugador.objects.create_object(dorsal, nombre, apellido, posicion)
			objeto.save()

	posiciones = models.Posicion.objects.all()
	plantilla = 'jugador/editar.html'
	return render(request, plantilla, {'objeto':objeto, 'mensaje':mensaje, 'posiciones':posiciones})


def jugador_nuevo(request):
	mensaje = ''
	if request.method == "POST":
		try:
			
			dorsal = ""
			nombre = ""
			apellido = ""
			posicion = models.Posicion

			objeto = models.Jugador
			if request.POST.get('dorsal', ''):
				dorsal = request.POST['dorsal'].upper()
				if request.POST.get('nombre', ''):
					nombre = request.POST['nombre'].upper()
					if request.POST.get('apellido', ''):
						apellido = request.POST['apellido'].upper()
						if request.POST.get('posicion', ''):
							posicion = posicion.objects.get(id=int(request.POST['posicion']))
							objeto = objeto.objects.get(dorsal=dorsal, nombre=nombre, apellido=apellido, posicion=posicion)
							mensaje = "Ya existe jugador con la información ingresada"
						else:
								mensaje = "Debe seleccionar la posicion del jugador"
					else:
						mensaje = "Debe ingresar el apellido del jugador"
				else:
					mensaje = "Debe ingresar el nombre del jugador"
			else:
				mensaje = "Debe ingresar la dorsal del jugador"
		except posicion.DoesNotExist:
			mensaje = "La posicion seleccionada no existe"
		except objeto.DoesNotExist:
			objeto = models.Jugador.objects.create_object(dorsal, nombre, apellido, posicion)
			objeto.save()
			return HttpResponseRedirect('/jugador/listado')

	posiciones = models.Posicion.objects.all()
	plantilla = 'jugador/nuevo.html'
	return render(request, plantilla, {'mensaje':mensaje, 'posiciones':posiciones})

def jugadores(request):
	listado = models.Jugador.objects.all()
	plantilla = 'jugador/lista.html'
	return render(request, plantilla, {'listado':listado})
