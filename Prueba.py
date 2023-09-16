import time 
from collections import deque
from Proceso import *
from random import *
import msvcrt
class Prueba:
    descartar = False
    acomodar = False
    pausa= False
    listaDeTerminados=[]
    cola=deque()
    cola1=deque()
    listaDeProcesos=deque()
    cuenta = 0
    def prueba(self):
        
        contador_gen = 0
        opc = int(input("Numero de registros "))
        for i in range(opc):
            proceso=Proceso()
            proceso.oper =randrange(1,7)
            proceso.n1 = randrange(1,100)
            proceso.n2= randrange(1,100)
            self.operaciones(proceso)
            proceso.eta=5
            contador_gen=contador_gen+ proceso.eta 
            proceso.id= "N" + str(i+1)
            self.listaDeProcesos.append(proceso)
        self.imprimir(self.listaDeProcesos)
    def  doDescartar(self):
        self.descartar = True
    def  doAcomodar(self):
        self.acomodar = True
    def  doPausa(self):
        self.pausa = True

    def operaciones(self,proceso):
        if(proceso.oper== 1):
                proceso.res = proceso.n1 + proceso.n2       
        if(proceso.oper== 2):
                proceso.res = proceso.n1 - proceso.n2
        if(proceso.oper== 3):
                proceso.res = proceso.n1 * proceso.n2
        if(proceso.oper== 4):
                proceso.res = proceso.n1 / proceso.n2
        if(proceso.oper==5):
                proceso.res = proceso.n1 // proceso.n2
        if(proceso.oper== 6):
                proceso.res = proceso.n1 % proceso.n2
        if(proceso.oper== 7):
                proceso.res = proceso.n1 ** proceso.n2

    def imprimir(self,listaDeProcesos):

        
        while(len(listaDeProcesos) > 0): #acabar los elementos de la lista
            self.cola.clear()
            self.cola1.clear()
            for a in range(5):#añadir lote a la cola 
                self.cola.append(listaDeProcesos[0])
                listaDeProcesos.popleft()

                if(len(listaDeProcesos) == 0):#termina si la listadeprocesos tiene un lote sin llenar 
                        break
            while len(self.cola)>0:
                resultado=self.procesamiento()
                self.cola.clear()
                if len(resultado)>0:
                    self.cola=resultado

            self.terminados()
   
    def procesamiento(self):
          interrupters=deque()
          total=len(self.listaDeProcesos)
          for p in range(len(self.cola)):
                    i=self.cola[p]
                    if(total==5 or total==10 or total==15):
                        print("No. Lotes pendientes \n" ,(total//5)-1 )
                    print("No. Lotes pendientes \n" ,total//5 )
                    print("Pendientes ")
                    """if(len(self.cola1)!=0):
                        self.cola1.popleft()
                    for p in self.cola1:
                        print("ID ",p.id, "Time" ,p.eta,"\n") #imprime los pendientes """

                    print("Actual")
                    
                    for i.contador in range(i.eta):#proceso en ejecucion + contado AQUI VA LA INTERRUPCION DEL TECLADO
                        self.cuenta=self.cuenta + 1
                        if(i.oper ==1):
                            print("ID ", i.id, " Ope  ", i.n1," + ",i.n2,"\n")
                        if(i.oper ==2):
                            print("ID ", i.id, " Ope  ", i.n1," - ",i.n2,"\n") 
                        if(i.oper ==3):
                            print("ID ", i.id,  " Ope  ", i.n1," * ",i.n2,"\n") 
                        if(i.oper ==4):
                            print("ID ", i.id,  " Ope  ", i.n1," / ",i.n2,"\n")
                        if(i.oper ==5):
                            print("ID ", i.id, " Ope  ", i.n1," // ",i.n2,"\n")
                        if(i.oper ==6):
                            print("ID ", i.id,  "Ope ", i.n1," % ",i.n2,"\n")  
                        print("Tiempo total  " ,i.eta , "   Tiempo Transcurrido  " , i.contador , "   Tiempo Restante  " ,i.eta - i.contador, "Contador", self.cuenta)

                        time.sleep(2)
                        if i.contador == i.eta-1:
                             self.listaDeTerminados.append(i)
                        if self.descartar == True:
                             self.descartar = False
                             self.listaDeTerminados.append(i)
                             i.oper=10
                             break
                        if self.acomodar == True:
                             self.acomodar = False
                             i.eta=i.eta-i.contador
                             interrupters.append(i)
                             break
                        if self.pausa == True:
                             pausa = msvcrt.getch()
                             while (pausa != b'c'):
                                  pausa = msvcrt.getch()
                             self.pausa = False
          return interrupters
    def terminados(self):
        print("Terminados")
        for i in self.listaDeTerminados:
            if(i.oper ==1):
                print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res ,"\n")
            if(i.oper ==2):
                print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res ,"\n")
            if(i.oper ==3):
                print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res ,"\n")
            if(i.oper ==4):
                print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res ,"\n")
            if(i.oper ==5):
                print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res ,"\n")
            if(i.oper ==6):
                print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res ,"\n")
            if(i.oper ==10):
                print("ID   " ,i.id, "ERROR" "\n")
        #self.total=self.total-1

                             
                
                    