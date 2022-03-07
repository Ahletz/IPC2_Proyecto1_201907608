
from ListasLink import *
from CargaArchivo import Carga
from xml.dom import minidom


class Datos:

    def __init__(self) :
        print('SELECCIONE SU ARCHIVO EN LA PESTAÑA: \n')

    def Open (self):

        #llamado de la ventana para poder obtener el enlace del archivo xml
        sun = Carga()
        sun.AbrirVentana()
        link = str(sun.direccion) #direccion del documento xml
        
        #utilizar minidom para poder utilizar datos del archivo 
        doc = minidom.parse(link)

        lista = ListasEnlazadas() #lista con datos de pisos 
        pisos = ListasEnlazadaN() #lista con nombres de pisos
        matriz = ListasEnlazadaM() #lista con datos de patrones pisos y posicion 


        #datos extraidos del documento xml
        nombre = doc.getElementsByTagName("piso")
        lineas = doc.getElementsByTagName("R")
        columnas = doc.getElementsByTagName("C")
        volteo = doc.getElementsByTagName("F")
        cambio = doc.getElementsByTagName("S")
        patron = doc.getElementsByTagName("patrones")

        
            #envio de iformacion a lista enlazada 
        for x in range(len(nombre)):

            name = nombre[x].attributes['nombre'].value #nombre del piso 
            line = lineas[x].firstChild.data #cantidad de lineas
            colum = columnas[x].firstChild.data #cantidad de columnas
            swap= volteo[x].firstChild.data #costo giro 
            switch = cambio[x].firstChild.data #costo cambio 
            cod = patron[x].getElementsByTagName("patron")
            
            lista.Agregar(name, line, colum, swap, switch) #agregar datos a lista principal

            #agregar nombres de patrones y pisos a los que pertenecen 
            for y in range(len(cod) ):

                nombrepatron = cod[y].attributes['codigo'].value 
                pat = cod[y].firstChild.data 
                nombrepiso = nombre[x].attributes['nombre'].value
                

                pisos.Agregar(nombrepatron,nombrepiso)

                posx = 1
                posy = 1
                 #agregar los patrones y el nombre al patron que pertenecen 
                for z in range(len(pat)):
                    if posx <= int(colum) and posy <= int(len(line)):

                        dato = pat[z]
                        matriz.Agregar(posx, posy, dato, nombrepatron)
                        posx+=1
                    else:
                        posx = 1
                        posy +=1
                        dato = pat[z]
                        matriz.Agregar(posx, posy, dato, nombrepatron)
                        posx+=1

        

        menu = True
        pisos_eleccionado = ''
        patron_seleccionado =''
        
        print('=== Bienvenido al menu de seleccion!===\n')

        print('    //////\ \   ')
        print('   /          \ ')
        print(' _|   _   _   |_')
        print('|.| -(.)-(.)- |.|')
        print(' \|     J     |/')
        print('  \    ---    / ')
        print('   \         / ')
        print('     "####"  \n')

        while menu ==True:
           

            print('== Seleccione la accion a realizar: ')
            print('|| 1. Seleccionar piso.               ||')
            print('|| 2. Seleccionar codigo a modificar. ||')
            print('|| 3. Ingresar codigo nuevo.          ||')
            print('|| 4. salir                           ||')

            opcion = int(input())

            if opcion == 1:
                print('USTED ELIGIO LA OPCION NUMERO 1\n')

                lista.Imprimir_Nombres_Pisos()#imprimir los nombres de los pisos existentes

                print('')
                print('|| INGRESE EL NOMBRE DEL PISO SELECCIONADO: \n')

                pisos_eleccionado = input() #ingresar nombre de piso seleccionado 

                lista.Piso_seleccionado(pisos_eleccionado)

                continue
            elif opcion == 2: 

                print('USTED ELIGIO LA OPCION NUMERO 2\n')

                pisos.Imprimir_nombre_codigo(pisos_eleccionado) #impresion de codigos respecto al piso

                print('|| INGRESE EL NOMBRE DEL CODIGO SELECCIONADO: \n')

                codigo_seleccionado = input() #ingresar codigo seleccionado
                print('')

                pisos.Codigo_Seleccionado(pisos_eleccionado,codigo_seleccionado)

                matriz.Imprimir(codigo_seleccionado)
                print('')


            elif opcion == 3: 
                print('USTED ELGJIO LA OPCION NUMERO 4 \n')
                print('INGRESE EL NUEVO PATRON : ')
                nuevo_patron = input()

            elif opcion == 4: 
                print('REDIRIGUIENDO A MENU PRINCIPAL...\n')
                menu = False
            else: 
                print('NO INGRESO UNA OPCION VALIDA.')


            



            
        
                









        

        

        
        
        
        

        






    

    




