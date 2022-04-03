class Nodo:
    def __init__(self,unidadm, filas,columnas):
        self.unidadm=unidadm
        self.filas=filas
        self.columnas=columnas
        self.sig=None
class ListaSimpleUM:
    def __init__(self):
        self.cabeza=None
        self.size=0
    def insertar(self,unidadm,filas,columnas):
        nuevo=Nodo(unidadm, filas,columnas)
        if not self.cabeza:
            self.cabeza=nuevo
            self.size+=1
            return
        actual=self.cabeza
        while actual.sig:
            actual=actual.sig
        actual.sig=nuevo
        self.size+=1
    def buscar(self, fila,columna):
        actual = self.cabeza
        while actual != None:
            if fila == actual.filas and columna==actual.columnas:
                return actual
            actual = actual.sig