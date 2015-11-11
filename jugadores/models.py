#encoding:utf-8
from django.db import models

#Manager Posicion .
class PosicionManager(models.Manager):
	def create_object(self, nombre):
		objeto = self.create(nombre = nombre)
		return objeto

#Modelo Posicion
class Posicion(models.Model):
	nombre = models.CharField(max_length=100, null=False, unique=True)
	objects = PosicionManager()

	def __str__(self):
		return self.nombre

#Manager Jugador .
class JugadorManager(models.Manager):
	def create_object(self, dorsal, nombre, apellido, posicion):
		objeto = self.create(dorsal = dorsal, nombre = nombre, apellido = apellido, posicion = posicion)
		return objeto

#Modelo Jugador
class Jugador(models.Model):
	dorsal = models.CharField(max_length=3, null=False, unique=True)
	nombre = models.CharField(max_length=100, null=False)
	apellido = models.CharField(max_length=100, null=False)
	posicion = models.ForeignKey(Posicion)
	objects = JugadorManager()

	def __str__(self):
		return self.nombre + " - " + self.apellido