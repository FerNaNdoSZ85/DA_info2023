import os

import funciones
from def_funciones.validacion import menu
from var import variables as V

fin = False
while not fin:
	os.system('cls' if os.name=='nt' else 'clear')
	print("==================================")
	print("=         MI PRIMER API          =")
	print("==================================")
	opcion = menu(V.MENU) # al menu debo le paso el argumento, en este caso el nombre de la funcion seleccionada
	getattr(funciones, V.MENU[opcion]["funcion"])()