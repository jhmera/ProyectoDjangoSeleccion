"""seleccion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from jugadores import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

	#GENERAL
	url(r'^$', views.home),

    #ESPECIE
    url(r'^posicion/(\d{1,10})/$', views.posicion),
    url(r'^posicion/editar/(\d{1,10})/$', views.posicion_editar),
    url(r'^posicion/listado$', views.posiciones),
    url(r'^posicion/nuevo$', views.posicion_nuevo),
    
    #ALIMENTO
    url(r'^jugador/(\d{1,10})/$', views.jugador),
    url(r'^jugador/editar/(\d{1,10})/$', views.jugador_editar),
    url(r'^jugador/listado$', views.jugadores),
    url(r'^jugador/nuevo$', views.jugador_nuevo),

]
