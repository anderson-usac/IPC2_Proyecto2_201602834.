class Vertice:
    def __init__(self,i):
        self.id=i
        self.siguientes=[]
        self.visitado=False
        self.padre=None
        self.distancia=float('inf')
    
    def agregarSiguientes(self,v,p):
        if v not in self.siguientes:
            if p=='*':
                p=-1
                self.siguientes.append([v,p])
        
class Camino:
    def __init__(self):
        self.vertices={}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id]=Vertice(id)
    
    def agregarArista(self,a,b,p):
        if p=='*':
            p=-1
            if a in self.vertices and b in self.vertices:
                self.vertices[a].agregarVecino(b,p)
                self.vertices[b].agregarVecino(a,p)
    
    def camino(self,a,b):
        camino=[]
        actual=b
        while actual!= None:
            camino.insert(0,actual)
            actual=self.vertices[actual].padre
        return(camino,self.vertices[b].distancia)

    def minimo(self,l):
        if len(l)>0:
            m= self.vertices[l[0]].distancia
            v=l[0]
            for k in l:
                if m> self.vertices[k].distancia:
                    m=self.vertices[e].distancia
                    v=k
            return v

    def dijkstra(self,a):
        if a in self.vertices:
            self.vertices[a].distancia=0
            actual=a
            noVisitados=[]
            for v in self.vertices:
                if v!=a:
                    self.vertices[v].distancia=float('inf')
                self.vertices[v].padre=None
                noVisitados.append(v)

            while len(noVisitados)>0:
                for sig in self.vertices[actual].siguientes:
                    if self.vertices[sig[0]].visitado==False:
                        if self.vertices[actual].distancia+sig[1]<self.vertices[sig[0]].distancia:
                            self.vertices[sig[0]].distancia=self.vertices[actual].distancia+sig[1]
                            self.vertices[sig[0]].padre=actual
                self.vertices[actual].visitado=True
                noVisitados.remove(actual)

                actual=self.minimo(noVisitados)
        else:
            return False