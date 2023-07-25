import sys

from peticiones.obj_req import *
from peticiones.POKE_APIs import *


#? Definicion de las opciones de consultas a la API
def solicitud_planetas():
	print("prueba si ejecuta la funcion_ solicitud_planetas")
	Peticiones.planetas()

def solicitud_species():
	print("prueba si ejecuta la funcion_solicitud_species")
	Peticiones.species()

def solicitud_population():
	print("prueba si ejecuta la funcion_solicitud_poblacion")
	Peticiones.population()

def solicitud_starships():
	print("prueba si ejecuta la funcion_solicitud_naves_espaciales")
	Peticiones.starships()

def solicitud_vehicles():
	print("prueba si ejecuta la funcion_solicitud_vehiculos")
	Peticiones.vehicles()

def salir():
	print("consultas finalizadas")
	sys.exit()
