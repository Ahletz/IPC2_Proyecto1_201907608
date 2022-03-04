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
        patron = doc.getElementsByTagName("patron")

        
            #envio de iformacion a lista enlazada 
        for x in range(len(nombre)):

            name = nombre[x].attributes['nombre'].value
            line = lineas[x].firstChild.data
            colum = columnas[x].firstChild.data
            swap= volteo[x].firstChild.data
            switch = cambio[x].firstChild.data

            lista.Agregar(name, line, colum, swap, switch) #agregar datos a lista principal

            for y in range(len(patron)):

                nombrepatron = patron[y].attributes['codigo'].value
                pat = patron[y].firstChild.data

                pisos.Agregar(nombrepatron)

                posx = 1
                posy = 1
                for z in range(len(pat)):
                    if posx <= int(line):

                        dato = pat[z]
                        matriz.Agregar(posx, posy, dato)
                        posx+=1
                    else:
                        posx = 1
                        posy +=1
                









        

        

        
        
        
        

        






    

    




