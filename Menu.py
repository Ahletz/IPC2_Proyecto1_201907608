from ManejoXML import *
from ListasLink import *

from CargaArchivo import Carga


class Presentacion():

    def __init__(self) :
        print ('===========BIENVENIDO===========\n')

    def PrestencaionOpciones(self):

        ciclo = True #condicion ciclo menu 
        while ciclo == True: #ciclo para la repeticion del menu hasta terminar el programa

            print('SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: ')
            print('|| 1. CARGAR ARCHIVO.                 ||')
            print('|| 2. SALIR.                          ||')

            opcion = int(input())

            if opcion == 1:
                print('USTED ELIJIO LA OPCION NUMERO 1\n')
               
                #prueba xml 
                prueba = Datos()
                prueba.Open()

                continue
            elif opcion == 2: 
                print('USTED ELIJIO LA OPCION NUMERO 3')
                ciclo = False
            else: 
                print('NO INGRESO UNA OPCION VALIDA.')

    

    

        
 
                
    