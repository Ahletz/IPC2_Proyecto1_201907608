from traceback import print_tb
from numpy import minimum

from CargaArchivo import Carga


class Presentacion():

    def __init__(self) :
        print ('===========BIENVENIDO===========\n')

    def PrestencaionOpciones(self):

        ciclo = True #condicion ciclo menu 
        while ciclo == True: #ciclo para la repeticion del menu hasta terminar el programa

            print('SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: ')
            print('|| 1. CARGAR ARCHIVO.                 ||')
            print('|| 2. SELECCIONAR UN PATRON Y PISO.   ||')
            print('|| 3. SALIR.                          ||')

            opcion = int(input())

            if opcion == 1:
                print('USTED ELIJIO LA OPCION NUMERO 1')
                carga = Carga()
                carga.AbrirVentana()
                archivo = carga.direccion
                print(archivo)
                continue
            elif opcion ==2:
                print('USTED ELIJIO LA OPCION NUMERO 2')
                self.minimenu()
                continue
            elif opcion == 3: 
                print('USTED ELIJIO LA OPCION NUMERO 3')
                ciclo = False
            else: 
                print('NO INGRESO UNA OPCION VALIDA.')

    #metodo para submenu de la opcion 2
    def minimenu(self):
        print('seleccionaste el minimenu ')
 
                
    