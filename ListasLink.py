
#clase para la creacion del nodo de la lista enlazada 
class Nodo:

    def __init__(self, value):
        self.value = value
        self.Siguiente = None

    def __str__(self):

        return str(self.value)
 #formacion de las listas enlazadas 
class ListasEnlazadas:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self, value):

        NuevoNodo= Nodo(value)

        if self.Tamaño == 0:
            self.Primero = NuevoNodo
        else:
            current = self.Primero
            while current.Siguiente != None:
                current = current.Siguiente
            current.Siguiente = NuevoNodo
        
        self.Tamaño+=1
        return NuevoNodo
    
    def Eliminar(self, value):
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
        return DeletedNode

    def TL(self):
        return self.Tamaño

    





                

        
        