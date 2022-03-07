
#clase para la creacion del nodo de la lista enlazada 
from textwrap import indent
from xml.etree.ElementInclude import include


class Nodo:

    def __init__(self, nombre, fila, columna, volteo, cambio):
        self.nombre = nombre
        self.fila = fila 
        self.columna = columna
        self.volteo = volteo
        self.cambio = cambio
        self.Siguiente = None

    def __str__(self):

        return str(self.nombre, self.fila, self.columna, self.volteo, self.cambio)

 #formacion de las listas enlazadas 
class ListasEnlazadas:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self, nombre, fila, columna, volteo, cambio):

        NuevoNodo= Nodo( nombre, fila, columna, volteo, cambio)

        if self.Tamaño == 0:
            self.Primero = NuevoNodo
        else:
            current = self.Primero
            while current.Siguiente != None:
                current = current.Siguiente
            current.Siguiente = NuevoNodo
        
        self.Tamaño+=1
        return NuevoNodo
        
    
    '''def Eliminar(self, value): #funcion para eliminar un nodo 
        if self.Tamaño ==0:
            return False
        else: 
            current = self.Primero
            while current.Siguiente.value != value:
                if current.Siguiente == None:
                    return False
                else:
                    current = current.Siguiente
                DeletedNode = current.Siguiente
                current.Siguiente = DeletedNode.Siguiente
        self.Tamaño -=1
        return DeletedNode'''

    def TL(self): #tamaño de la lista
        return self.Tamaño

    def Imprimir_Nombres_Pisos(self):

        puntero = self.Primero
        indice = 1

        while puntero != None:
            print(str(indice)+'. '+puntero.nombre)
            puntero = puntero.Siguiente
            indice +=1
        print('')
    
    def Piso_seleccionado(self, piso_seleccionado):

        puntero = self.Primero
        self.piso_seleccionado = piso_seleccionado
        encontrado = False

        while encontrado ==False:
            if puntero != None:
                if piso_seleccionado == puntero.nombre:
                    print('|| PISO SELECCIONADO CORRECTAMENTE! \n')
                    encontrado = True
                else: 
                    puntero = puntero.Siguiente
            else:
                print('|| EL PISO QUE INGRESO NO ES VALIDO. \n')
                encontrado = True

    

#lista con los nombres de los codigos que contiene cada piso 
class NodoN:

    def __init__(self, nombre, nombrepiso):
        self.nombre = nombre
        self.nombrepiso  = nombrepiso 
        self.Siguiente = None

    def __str__(self):

        return str(self.nombre,self.nombrepiso)

 #formacion de las listas enlazadas 
class ListasEnlazadaN:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,  nombre, nombrepiso):

        NuevoNodo= NodoN( nombre, nombrepiso)

        if self.Tamaño == 0:
            self.Primero = NuevoNodo
        else:
            current = self.Primero
            while current.Siguiente != None:
                current = current.Siguiente
            current.Siguiente = NuevoNodo
        
        self.Tamaño+=1
        return NuevoNodo
        

    def TL(self): #tamaño de la lista
        return self.Tamaño

    def Imprimir_nombre_codigo(self, nombre_piso):

        puntero = self.Primero
        indice = 1

        self.nombre_piso = nombre_piso #nombr del piso del que se seleccinara el patron 

        while puntero != None:
            if nombre_piso == puntero.nombrepiso: #condicinal para encontrar el nombre del codigo correspondiente al piso 
                print(str(indice)+'. '+puntero.nombre) #impresion del nombre del codigo en el piso correspondiente
                indice +=1
                puntero = puntero.Siguiente
            else:
                puntero = puntero.Siguiente
        
    
    def Codigo_Seleccionado(self,nombrepiso, nombre_codigo):

        puntero = self.Primero
        self.nombrepiso = nombrepiso
        self.nombre_codigo = nombre_codigo

        encontrado = False

        while encontrado == False: 

            if puntero != None:

                if nombrepiso == puntero.nombrepiso and nombre_codigo == puntero.nombre:

                    print('|| CODIGO SELECCIONADO CORRECTAMENTE! \n')

                    encontrado = True
                else:
                    puntero = puntero.Siguiente
            else:
                print('|| EL CODIGO INGRESADO NO ES VALIDO.')
                encontrado = True


        


# lista con los codigos contiene cada piso 
class NodoM:

    def __init__(self, posicionx, posiciony, dato, codigo):
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.dato = dato
        self.codigo = codigo
        self.Siguiente = None

    def __str__(self):

        return str(self.posicionx,self.posicionx, self.dato, self.codigo)

 #formacion de las listas enlazadas 
class ListasEnlazadaM:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,   posicionx, posiciony, dato, codigo):

        NuevoNodo= NodoM(posicionx, posiciony, dato, codigo)

        if self.Tamaño == 0:
            self.Primero = NuevoNodo
        else:
            current = self.Primero
            while current.Siguiente != None:
                current = current.Siguiente
            current.Siguiente = NuevoNodo
        
        self.Tamaño+=1
        return NuevoNodo
        

    def TL(self): #tamaño de la lista
        return self.Tamaño
    
    def Imprimir(self, Nombre_codigo):

        patron = '' #variable que contendra los datos de la matriz 
        matriz = '{' #variable con la matriz 
        puntero = self.Primero
        self.nombre_codigo = Nombre_codigo

        while puntero != None:

            if Nombre_codigo == puntero.codigo:
                patron += puntero.dato

                matriz +='['
                matriz +=str(puntero.posicionx)
                matriz +=', '
                matriz +=str(puntero.posiciony)
                matriz +=' - '
                matriz +=puntero.dato
                matriz +='] '

                puntero = puntero.Siguiente
            else: 
                puntero= puntero.Siguiente
        matriz +='}'
        print(patron)
        print('')
        print('DE MATRIZ: \n')
        print(matriz)

            





        
            
        
        
        


            
        
    





                

        
        