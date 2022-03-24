import os
import webbrowser
class Nodoi(): #Nodo que guarda las cantidades de combustible
    def __init__(self,fila,columna,atributo):
        self.atributo=atributo
        self.fila=fila
        self.columna=columna
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None
class nodoencabezado: #lista doble enlazada para las cabeceras
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.acceso=None
    
class listaencabezado:
    def __init__(self,primero=None):
        self.primero=primero
    
                
    def crearencabezado(self,nuevo):
        if (self.primero==None):
            self.primero=nuevo
        elif(nuevo.id < self.primero.id):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente !=None:
                if(nuevo.id<actual.siguiente.id):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente
            if(actual.siguiente==None):
                actual.siguiente=nuevo
                nuevo.anterior=actual
    def obtenerencabezado(self,id): #retorna el numero de encabezados
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None
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

    def recorrer(self):
        nodo_act = self.encabezadof.primero
        while nodo_act is not None:
            fila = nodo_act.acceso
            while fila is not None:
                print('|'+fila.atributo, end='')
                fila = fila.derecha
            print("|")
            nodo_act = nodo_act.siguiente

    def graficarterreno(self):
        grap='''digraph T{ node[shape=circle fontname="Arial" fillcolor="white" style=filled ]
            root[label = "raiz"]
            subgraph cluster_p{\n'''
        grap+='''\t\t\t\tlabel = "{}"
                fontname="Arial Black"
                fontsize="20pt"
                edge[dir="none"]\n'''.format(self.nombre)
        hfilas=self.encabezadof.primero
        while hfilas != None:
            grap+='F{}[label="{}",fillcolor="skyblue",group=1];\n'.format(hfilas.id,hfilas.id)
            hfilas= hfilas.siguiente

        hfilas=self.encabezadof.primero
        while hfilas !=None:
            if hfilas.siguiente!=None:
                grap+='F{}->F{};\n'.format(hfilas.id,hfilas.siguiente.id)
            hfilas=hfilas.siguiente
        hcolumnas=self.encabezadoc.primero
        while hcolumnas!=None:
            group=int(hcolumnas.id)+1
            grap+='C{}[label="{}",fillcolor="yellow",group={}];\n'.format(hcolumnas.id,hcolumnas.id,str(group))
            hcolumnas=hcolumnas.siguiente
        cont=0
        hcolumnas=self.encabezadoc.primero
        while hcolumnas is not None:
            if hcolumnas.siguiente is not None:
                grap+='C{}->C{}\n'.format(hcolumnas.id,hcolumnas.siguiente.id)
            cont+=1
            hcolumnas=hcolumnas.siguiente
        hcolumnas=self.encabezadoc.primero
        hfilas=self.encabezadof.primero
        grap+='root->F{};\n root->C{};\n'.format(hfilas.id,hcolumnas.id)
        grap+='{rank=same;root;'
        cont=0
        hcolumnas=self.encabezadoc.primero
        while hcolumnas != None:
            grap+='C{};'.format(hcolumnas.id)
            cont+=1
            hcolumnas=hcolumnas.siguiente
        grap+='}\n'
        aux=self.encabezadof.primero
        aux2=aux.acceso
        cont=0
        while aux != None:
            cont+=1
            while aux2 != None:
                grap+='N{}_{}[label="{}",group="{}"];\n'.format(aux2.fila,aux2.columna,aux2.combustible,int(aux2.columna)+1)
                aux2=aux2.derecha
            aux=aux.siguiente
            if aux !=None:
                aux2=aux.acceso
        aux=self.encabezadof.primero
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
        aux=self.encabezadoc.primero
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

        filegrap=open('grafica.txt','w')
        filegrap.write(grap)
        filegrap.close()
        hola="grafica.txt"
        hol="matriz.jpg"
        os.system("dot -Tjpg " +hola+  " -o "+hol)
        print('')
        print("Ahorita te lo abro XD")
        webbrowser.open(hol)