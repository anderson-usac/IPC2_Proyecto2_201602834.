import os
import webbrowser
from NodosEncabezado import listaencabezado,nodoencabezado
class Nodoi(): #Nodo que guarda las cantidades de combustible
    def __init__(self,fila,columna,atributo):
        self.atributo=atributo
        self.fila=fila
        self.columna=columna
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None

class Matriz:
    def __init__(self):
        self.encabezadof=listaencabezado()
        self.encabezadoc=listaencabezado()
        self.nombre=None

    def insertar(self,nombre,fila,columna,atributo):
        self.nombre=nombre
        nuevo=Nodoi(fila,columna,atributo) 
        encabezadof=self.encabezadof.obtenerencabezado(fila)
        if( encabezadof == None):                           
            encabezadof = nodoencabezado(fila)            
            encabezadof.acceso = nuevo
            self.encabezadof.crearencabezado(encabezadof)        
        else:                                      
            if nuevo.columna < encabezadof.acceso.columna: 
                nuevo.derecha = encabezadof.acceso     
                encabezadof.acceso.izquierda = nuevo
                encabezadof.acceso = nuevo
            else:
                actual = encabezadof.acceso
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha  
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo           
                    nuevo.izquierda = actual
        encabezadoc = self.encabezadoc.obtenerencabezado(columna)
        if encabezadoc == None:                           
            encabezadoc = nodoencabezado(columna)            
            encabezadoc.acceso = nuevo
            self.encabezadoc.crearencabezado(encabezadoc)        
        else:                                       
            if nuevo.fila < encabezadoc.acceso.fila: 
                nuevo.abajo = encabezadoc.acceso      
                encabezadoc.acceso.arriba = nuevo
                encabezadoc.acceso = nuevo
            else:
                actual = encabezadoc.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo  
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo            
                    nuevo.arriba = actual

    def buscar(self,fila,columna):
        encabezadoc=self.encabezadoc.primero
        while encabezadoc !=None:
            actual=encabezadoc.acceso
            while actual !=None:
                if actual.fila==fila and actual.columna==columna:
                    return actual.atributo
                actual=actual.abajo
            encabezadoc=encabezadoc.siguiente

    def modificar(self,fila,columna,nuevo):
        encabezadoc=self.encabezadoc.primero
        while encabezadoc !=None:
            actual=encabezadoc.acceso
            while actual !=None:
                if actual.fila==fila and actual.columna==columna:
                    actual.atributo=nuevo
                actual=actual.abajo
            encabezadoc=encabezadoc.siguiente


    def recorrer(self):
        nodo_act = self.encabezadof.primero
        while nodo_act is not None:
            fila = nodo_act.acceso
            while fila is not None:
                print('|'+fila.atributo, end='')
                fila = fila.derecha
            print("|")
            nodo_act = nodo_act.siguiente

    def graficarciudad(self,nombre,matriz):
        matriz.recorrer()
        grap='''digraph T{ node[shape=box fontname="Arial" fillcolor="white" style=filled ]
            root[label = "raiz"]
            subgraph cluster_p{\n'''
        grap+='''\t\t\t\tlabel = "{}"
                fontname="Arial Black"
                fontsize="20pt"
                ranksep="0 equally"
                edge[dir="none"]\n'''.format(nombre)
        hfilas=matriz.encabezadof.primero
        while hfilas != None:
            grap+='F{}[label="{}",fillcolor="skyblue",group=1];\n'.format(hfilas.id,hfilas.id)
            hfilas= hfilas.siguiente

        hfilas=matriz.encabezadof.primero
        while hfilas !=None:
            if hfilas.siguiente!=None:
                grap+='F{}->F{};\n'.format(hfilas.id,hfilas.siguiente.id)
            hfilas=hfilas.siguiente
        hcolumnas=matriz.encabezadoc.primero
        while hcolumnas!=None:
            group=int(hcolumnas.id)+1
            grap+='C{}[label="{}",fillcolor="yellow",group={}];\n'.format(hcolumnas.id,hcolumnas.id,str(group))
            hcolumnas=hcolumnas.siguiente
        cont=0
        hcolumnas=matriz.encabezadoc.primero
        while hcolumnas is not None:
            if hcolumnas.siguiente is not None:
                grap+='C{}->C{}\n'.format(hcolumnas.id,hcolumnas.siguiente.id)
            cont+=1
            hcolumnas=hcolumnas.siguiente
        hcolumnas=matriz.encabezadoc.primero
        hfilas=matriz.encabezadof.primero
        grap+='root->F{};\n root->C{};\n'.format(hfilas.id,hcolumnas.id)
        grap+='{rank=same;root;'
        cont=0
        hcolumnas=matriz.encabezadoc.primero
        while hcolumnas != None:
            grap+='C{};'.format(hcolumnas.id)
            cont+=1
            hcolumnas=hcolumnas.siguiente
        grap+='}\n'
        aux=matriz.encabezadof.primero
        aux2=aux.acceso
        cont=0
        while aux != None:
            cont+=1
            while aux2 != None:
                val=aux2.atributo
                if val=='*':
                    color='black'
                elif val=='R':
                    color='gray'
                elif val=='C':
                    color='blue'
                elif val=='E':
                    color='green'
                elif val.isdigit():
                    color='red'
                else:
                    color='white'
                grap+='N{}_{}[label="{}",fillcolor="{}",group="{}"];\n'.format(aux2.fila,aux2.columna,aux2.atributo,color,int(aux2.columna)+1)
                aux2=aux2.derecha
            aux=aux.siguiente
            if aux !=None:
                aux2=aux.acceso
        aux=matriz.encabezadof.primero
        aux2=aux.acceso
        cont=0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.id};'
            cont=0
            while aux2!=None:
                if cont==0:
                    grap+='F{}->N{}_{};\n'.format(aux.id,aux2.fila,aux2.columna)
                    cont+=1
                if aux2.derecha!=None:
                    grap+='N{}_{}->N{}_{};\n'.format(aux2.fila,aux2.columna,aux2.derecha.fila,aux2.derecha.columna)

                rank+='N{}_{};'.format(aux2.fila,aux2.columna)
                aux2=aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grap+= rank+'}\n' 
        aux=matriz.encabezadoc.primero
        aux2=aux.acceso
        cont=0
        while aux!=None:
            cont=0
            grap+=''      
            while aux2!=None:
                if cont==0:
                    grap+='C{}->N{}_{};\n'.format(aux.id,aux2.fila,aux2.columna)
                    cont+=1
                if aux2.abajo!=None:
                    grap+='N{}_{}->N{}_{};\n'.format(aux2.abajo.fila,aux2.abajo.columna,aux2.fila,aux2.columna)
                aux2=aux2.abajo
            aux=aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grap += '}\n}'

        filegrap=open('{}.txt'.format(nombre),'w')
        filegrap.write(grap)
        filegrap.close()
        hola="{}.txt".format(nombre)
        hol="{}.jpg".format(nombre)
        os.system("dot -Tjpg " +hola+  " -o "+hol)
        print('')
        print("Ahorita te lo abro Jefecito XD")
        webbrowser.open(hol)

# if __name__ == "__main__":
#     MatrizH=Matriz()
#     MatrizH.insertar('C1',8,5,'AA')
#     MatrizH.insertar('C1',6,5,'**')
#     MatrizH.insertar('C1',2,3,'**')
#     MatrizH.insertar('C1',7,4,'JJ')
#     MatrizH.modificar('8','5','AZ')
#     MatrizH.recorrer()
#     MatrizH.graficarciudad()

