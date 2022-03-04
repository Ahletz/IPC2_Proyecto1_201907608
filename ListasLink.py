
#clase para la creacion del nodo de la lista enlazada 
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

class NodoN:

    def __init__(self, nombre):
        self.nombre = nombre
        self.Siguiente = None

    def __str__(self):

        return str(self.nombre)

 #formacion de las listas enlazadas 
class ListasEnlazadaN:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,  nombre):

        NuevoNodo= NodoN( nombre)

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

class NodoM:

    def __init__(self, posicionx, posiciony, dato):
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.dato = dato
        self.Siguiente = None

    def __str__(self):

        return str(self.posicionx,self.posicionx, self.dato)

 #formacion de las listas enlazadas 
class ListasEnlazadaM:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,   posicionx, posiciony, dato):

        NuevoNodo= NodoM(posicionx, posiciony, dato)

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
    





                

        
        