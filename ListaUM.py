class Nodo:
    def __init__(self,nombre, tipo,capacidad):
        self.nombre=nombre
        self.tipo=tipo
        self.capacidad=capacidad
        self.sig=None
class ListaSimpleUM:
    def __init__(self):
        self.cabeza=None
        self.size=0
    def insertar(self,nombre,tipo,capacidad):
        nuevo=Nodo(nombre, tipo,capacidad)
        if not self.cabeza:
            self.cabeza=nuevo
            self.size+=1
            return
        actual=self.cabeza
        while actual.sig:
            actual=actual.sig
        actual.sig=nuevo
        self.size+=1
    def buscar(self,nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return actual
            actual = actual.sig

    def imprimir(self):
        actual=self.cabeza
        print('Robots disponibles:')
        while actual != None:
            print(actual.nombre,actual.tipo,actual.capacidad)
            actual=actual.sig