import os
import webbrowser
import tkinter.filedialog 
from xml.etree import ElementTree as ET
from xml.dom import minidom
from MatrizCiudad import Matriz




def readfile(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        xml_doc=file.read()
        root=ET.fromstring(xml_doc)
        for tag in root:
            if tag.tag=='listaCiudades':
                for stag in tag:
                    for subele in stag:
                        if subele.tag=='nombre':
                            ciudad=subele.text
                            filas=subele.attrib.get('filas')
                            columnas=subele.attrib.get('columnas')
                        elif subele.tag=='fila':
                            ff1=subele.text
                            cadfila=ff1.strip('"')
                            fila=subele.attrib.get('numero')
                            
                            print(fila)

                            

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
            pass
        elif opcion==5:
            exit()
        else:
            print("Opcion erronea")



if __name__ == "__main__":
    menu()