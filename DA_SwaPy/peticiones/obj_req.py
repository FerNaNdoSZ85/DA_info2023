import csv

import pandas as pd
import requests


def conexion_endpoint(pet_conexion):
    peticion = pet_conexion
    response = requests.get(peticion)
    contenido = response.json()
    # Verificar el código de estado de la respuesta
        
    if response.status_code == 200:
        # Mostrar el contenido de la respuesta
        print('*******************')
        print('peticion confirmada')
        print('*******************')
        #! para filtrar en primera instancia--> tomo la lista resultado del JSON
        dataf = contenido['results'] #! esta variable exporto a scv
        print("imprimo_dataf_ ")
        df = pd.json_normalize(dataf) #? imprimo esta variable usando json_normalize para que muestre todo en tabla
        print(df)
        exportar_scv(dataf)
    else:
        print('Error en la solicitud:', response.status_code)

class Peticiones:
    print ("Peticiones en curso")
    def planetas():
        print("conexion exitosa")
        pet_conexion = 'https://swapi.dev/api/planets/'
        conexion_endpoint (pet_conexion)

    def species():
        print("conexion exitosa")
        pet_conexion = 'https://swapi.dev/api/species/'
        conexion_endpoint (pet_conexion)

    def population():
        print("conexion exitosa")
        pet_conexion = 'https://swapi.dev/api/people/'
        conexion_endpoint (pet_conexion)
    
    def starships():
        print("conexion exitosa")
        pet_conexion = 'https://swapi.dev/api/starships/'
        conexion_endpoint (pet_conexion)
    
    def vehicles():
        print("conexion exitosa")
        pet_conexion = 'https://swapi.dev/api/vehicles/'
        conexion_endpoint (pet_conexion)

#! funcion de exportacion a scv
def exportar_scv(dataf):
    campos=[]
    a = input("desea exportar al formate scv? S/N: ").upper()
    if a == "S":
        with open ('data.csv', 'w') as file:
            campos = dataf[0].keys()
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for i in dataf:
                writer.writerow(i)
            print ("-= Exportacion Finalizada =-")
            aas= input("presione ENTER para continuar")
    else:
        aas= input("presione ENTER para continuar")
        pass