# Modulo de Validaciones de las opciones ingresadas
def es_correcto(valor, OPCIONES):
	return valor.isdigit() and int(valor) in OPCIONES.keys()

def menu(OPCIONES):
	print("Ingrese una de las siguientes opciones:")
	for key, value in OPCIONES.items():
		print("%s - %s" % (key, value["descripcion"]))
	
	opcion = input("\nIngrese una opcion: ")

	while not es_correcto(opcion, OPCIONES):
		print("Entrada incorrecta, ingrese un valor valido.")
		opcion = input("\nIngrese una opcion: ")

	return int(opcion)