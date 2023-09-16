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
    def prueba(self):
        listaDeProcesos=deque()
        contador_gen = 0
        opc = int(input("Numero de registros "))
        for i in range(opc):
            proceso=Proceso()
            proceso.oper =randrange(1,7)
            proceso.n1 = randrange(1,100)
            proceso.n2= randrange(1,100)
            self.operaciones(proceso)
            proceso.eta=randrange(4,6)
            contador_gen=contador_gen+ proceso.eta 
            proceso.id= "N" + str(i+1)
            listaDeProcesos.append(proceso)
        self.imprimir(listaDeProcesos)
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

        total=len(listaDeProcesos)
        while(len(listaDeProcesos) > 0): #acabar los elementos de la lista
            self.cola.clear()
            self.cola1.clear()
            for a in range(5):#añadir lote a la cola 
                self.cola.append(listaDeProcesos[0])
                self.cola1.append(listaDeProcesos[0])
                listaDeProcesos.popleft()
                cuenta = 0
                if(len(listaDeProcesos) == 0):#termina si la listadeprocesos tiene un lote sin llenar 
                        break
            
            for i in self.cola:
                    if(total==5 or total==10 or total==15):
                        print("No. Lotes pendientes \n" ,(total//5)-1 )
                    print("No. Lotes pendientes \n" ,total//5 )
                    print("Pendientes ")
                    if(len(self.cola1)!=0):
                        self.cola1.popleft()
                    for p in self.cola1:
                        print("ID ",p.id, "Time" ,p.eta,"\n") #imprime los pendientes 

                    print("Actual")
                    
                    for i.contador in range(i.eta):#proceso en ejecucion + contado AQUI VA LA INTERRUPCION DEL TECLADO
                        cuenta=cuenta + 1
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
                        print("Tiempo total  " ,i.eta , "   Tiempo Transcurrido  " , i.contador , "   Tiempo Restante  " ,i.eta - i.contador, "Contador", cuenta)
                        i.contador= i.contador
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
                             self.cola1.append(i)
                             self.cola1.popleft()
                             break
                        if self.pausa == True:
                             pausa = msvcrt.getch()
                             while (pausa != b'c'):
                                  pausa = msvcrt.getch()
                             self.pausa = False
                             
                        
                    cuenta=cuenta 
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
                    total=total-1
