import os
import webbrowser
import tkinter.filedialog 
from xml.etree import ElementTree as ET
from xml.dom import minidom
from MatrizCiudad import Matriz
from ListaUM import ListaSimpleUM


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
                return actual.matrizc
            actual = actual.sig   

    def imprimir (self):
        nodo=self.cabeza
        while nodo!=None:
            print(nodo.nombre,nodo.filas,nodo.columnas,nodo.matrizc.recorrer())
            nodo=nodo.sig

listaciudades=ListaSimple()
listarobots=ListaSimpleUM()  
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
            elif tag.tag=='robots':
                for subtag in tag:
                    for sstag in subtag:
                        if sstag.tag=='nombre':
                            tipo=sstag.attrib.get('tipo')
                            capacidad=sstag.attrib.get('capacidad')
                            nombrer=sstag.text
                            listarobots.insertar(nombrer,tipo,capacidad)                
                            
    listaciudades.imprimir()
    listarobots.imprimir()
    
                              
                            
def graficar():
    nombre=input('Ingrese nombre de la ciudad:')
    matrizaux=listaciudades.buscar(nombre)
    MatrizC.graficarciudad(nombre,matrizaux)


def misionrescate():
    nombre=input('Ingrese nombre de la ciudad:')
    matrizaux=listaciudades.buscar(nombre)
    disp=listarobots.buscar('ChapinRescue')
    print(disp)
    aux=matrizaux.encabezadof.primero
    aux2=aux.acceso
    cont=0
    while aux != None:
        cont+=1
        while aux2 != None:
            val=aux2.atributo
            if val=='C' and disp != None:
                print('Estos son los robots disponibles: ')
                print(disp)
                print('Se en contraron unidades civiles en ciudad {}: '.format(nombre))
                busqrobots=input('Ingrese el nombre del robot para la mision: ')
                robotres=listarobots.buscar2(busqrobots)
                print(robotres)
            else:
                print('¡¡MISION IMPOSIBLE!!')
            aux2=aux2.derecha
        aux=aux.siguiente
        if aux !=None:
            aux2=aux.acceso
    #MatrizC.misionR(nombre,matrizaux)
    

def misionextraccion():
    nombre=input('Ingrese nombre de la ciudad:')
    matrizaux=listaciudades.buscar(nombre)
    disp=listarobots.buscar('ChapinFighter')
    matrizrex=matrizaux.encabezadof.primero
    aux=matrizrex.acceso
    while matrizrex != None:
        while aux!=None:
            val=aux.atributo
            if val=='R' and disp != None:
                print('Estos son los robots disponibles: ')
                print(disp.nombre)
                print('Se en contraron unidades de recursos en ciudad {}: '.format(nombre))
            else:
                print('¡¡MISION IMPOSIBLE!!') 
            aux=aux.derecha
        matrizres=matrizres.siguiente
        if matrizrex !=None:
            aux=matrizrex.acceso


        


                            

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
        try:
            opcion = int(input("Ingrese opción: "))
        except:
            print('Ingrese solo las opciones del menú')
        if opcion==1:
            openfile()
        elif opcion==2:
            misionrescate()
        elif opcion==3:
           misionextraccion()
        elif opcion==4:
            graficar()
        elif opcion==5:
            exit()
        else:
            print("Opcion erronea")



if __name__ == "__main__":
    menu()