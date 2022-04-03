import os
import webbrowser
import tkinter.filedialog 
from xml.etree import ElementTree as ET
from xml.dom import minidom
from MatrizCiudad import Matriz
from ListaUM import ListaSimpleUM


MatrizJ=Matriz()
class Nodo:
    def __init__(self,nombre, filas,columnas):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.matrizc=Matriz()
        self.sig=None
class ListaSimple:
    def __init__(self):
        self.cabeza=None
        self.size=0
    def insertar(self,nombre,filas,columnas,matriz):
        nuevo=Nodo(nombre, filas,columnas)
        nuevo.matrizc=matriz
        if not self.cabeza:
            self.cabeza=nuevo
            self.size+=1
            return
        actual=self.cabeza
        while actual.sig:
            actual=actual.sig
        actual.sig=nuevo
        self.size+=1
    def buscar(self, nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return actual
            actual = actual.sig   

    def imprimir (self):
        nodo=self.cabeza
        while nodo!=None:
            print(nodo.nombre,nodo.filas,nodo.columnas,nodo.matrizc.recorrer())
            nodo=nodo.sig
listaciudades=ListaSimple()
listaUM=ListaSimpleUM()
def readfile(ruta):
    global listcad,cadfila,ciudad,filas,columnas,capum,ffum,ccum
    cadfila=[]
    with open(ruta,'r',encoding='utf-8') as file:
        cont=0
        cont1=0
        xml_doc=file.read()
        root=ET.fromstring(xml_doc)
        for tag in root:
            if tag.tag=='listaCiudades':
                for stag in tag:
                    global MatrizC
                    MatrizC=Matriz()
                    for subele in stag:
                        if subele.tag=='nombre':
                            ciudad=subele.text
                            filas=subele.attrib.get('filas')
                            columnas=subele.attrib.get('columnas')
                            #listaciudades.insertar(ciudad,filas,columnas)
                        elif subele.tag=='fila':
                            ff1=subele.text
                            cadfila=ff1.strip('"')
                            fila=subele.attrib.get('numero')
                            listcad=list(cadfila)
                            for c in range(len(cadfila)):
                                MatrizC.insertar(ciudad,int(fila),int(c)+1,cadfila[c])
                        elif subele.tag=='unidadMilitar':
                            capum=subele.text
                            ffum=subele.attrib.get('fila')
                            ccum=subele.attrib.get('columna')
                            MatrizC.modificar(int(ffum),int(ccum),capum)
                            
                            
                    listaciudades.insertar(ciudad,filas,columnas,MatrizC)
                            
                            
    listaciudades.imprimir()                            
                            
                            

                            

def openfile():
    global filename
    filename=''

    root = tkinter.Tk()
    root.withdraw()
    filters = (("Archivos xml", "*.xml"),("Ficheros de texto", "*.txt"),("all files", "*.*"))

    filename= tkinter.filedialog.askopenfilename(initialdir = "C:",filetypes = filters,)
    readfile(filename)



def menu():
    opcion=0
    while opcion!=5:
        print()
        print("  Menu Principal")
        print("————————————————————————")
        print(" 1.Cargar Archivo")
        print(" 2.Mision de Rescate")
        print(" 3.Mision de Extraccion")
        print(" 4.Generar Grafica")
        print(" 5.Salida ")
        print("————————————————————————")
        print(" >>Escoja una opcion")
        opcion = int(input("Ingrese opción: "))
        if opcion==1:
            openfile()
        elif opcion==2:
            pass
        elif opcion==3:
           pass
        elif opcion==4:
            MatrizC.graficarciudad()
        elif opcion==5:
            exit()
        else:
            print("Opcion erronea")



if __name__ == "__main__":
    menu()