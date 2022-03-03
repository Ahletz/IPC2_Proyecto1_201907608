from CargaArchivo import Carga
from xml.dom import minidom


class Datos:

    def __init__(self) :
        print('SELECCIONE SU ARCHIVO EN LA PESTAÑA: ')

    def Open (self):

        #llamado de la ventana para poder obtener el enlace del archivo xml
        sun = Carga()
        sun.AbrirVentana()
        link = str(sun.direccion)
        print(link)

        #utilizar minidom para poder utilizar datos del archivo 
        doc = minidom.parse(link)

        #datos extraidos del documento xml
        nombre = doc.getElementsByTagName("piso")
        lineas = doc.getElementsByTagName("R")
        columnas = doc.getElementsByTagName("C")
        volteo = doc.getElementsByTagName("F")
        cambio = doc.getElementsByTagName("S")
        patron = doc.getElementsByTagName("patron")

        for n in columnas:
            print(n.firstChild.data)

        

        
        
        
        

        






    

    




