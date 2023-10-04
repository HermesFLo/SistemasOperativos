import time 
from collections import deque
from Proceso import *
from random import *
import msvcrt
import threading
class Prueba:
    descartar = False
    acomodar = False
    pausa= False
    listaDeTerminados=[]
    cola=deque()
    listaDeProcesos=deque()
    cuenta = 0
    detenido=1
    bloqueados=deque()
    opc=int()
    def prueba(self):
        
        contador_gen = 0
        self.opc = int(input("Numero de registros "))
        for i in range(self.opc):
            proceso=Proceso()
            proceso.oper =randrange(1,6)
            proceso.n1 = randrange(1,100)
            proceso.n2= randrange(1,100)
            self.operaciones(proceso)
            proceso.eta=randrange(6,18)
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


    def imprimir(self,listaDeProcesos):
            for a in range(5):#añadir lote a la cola 
                self.cola.append(listaDeProcesos[0])
                listaDeProcesos.popleft()
                if(len(listaDeProcesos) == 0):#termina si la listadeprocesos tiene un lote sin llenar 
                        break
            for i in self.cola:
                 i.llegada= True
            while len(self.cola)>0:
                resultado=self.procesamiento()
            self.terminados()
         
    
    def procesamiento(self):
          espera=0# flag para guardar Tie Esp
          agregar = len(self.listaDeProcesos)-5
          interrupters=deque()
          rango=range(len(self.cola))
          flag= True
          llegada=0
          while len(self.listaDeTerminados) == self.opc:
                        total=len(self.listaDeProcesos)
                        i=self.cola.popleft()
                        print("No. Procesos nuevos  \n" , total)
                        print("Nuevos ")
                        for a in self.cola:
                            print("ID ",a.id, "Time" ,a.eta,"Tiempo Transcurrido",a.contador,"\n") #imprime los pendientes """
                            #a.tiempo_llegada=self.cuenta
                        if len(interrupters) >0:
                            for a in interrupters:
                                print("ID ",a.id, "Time" ,a.eta,"Tiempo Transcurrido",a.contador,"\n") #imprime los pendientes """
                                #a.tiempo_llegada=self.cuenta
                        self.terminados()
                        print("Actual")
                        espera=self.cuenta
                        for i.contador in range(i.eta):#proceso en ejecucion + contado AQUI VA LA INTERRUPCION DEL TECLADO
                            self.cuenta=self.cuenta + 1
                            i.tiempo_espera=self.cuenta+1
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
                            
                            if len(self.bloqueados)<=5:#Bloqueados
                                print("////////////////////////////BLOQUEOOOO///////////////////////////////////")
                                for b in self.bloqueados:
                                    print("ID ",b.id , "Tiempo Bloqueado ",b.tiempo_bloqueado )
                                    print("/////////////////////////////////////////////////////////////////////////\n\n")
                                    b.tiempo_bloqueado=b.tiempo_bloqueado +1
                                    if b.tiempo_bloqueado == 8:#para sacarlo de bloqueo
                                        b.bloqueo=b.bloqueo+1
                                        b.tiempo_bloqueado= 1
                                        self.cola.append(self.bloqueados.popleft())
                                        break
                            if i.contador == i.eta-1:#aregar a terminados
                                i.tiempo_final=self.cuenta
                                self.listaDeTerminados.append(i)
                                i.eta=i.contador
                                if len(self.listaDeProcesos)!=0:
                                    self.cola.append(self.listaDeProcesos[0])
                                    self.listaDeProcesos.popleft()
                                    i.tiempo_espera=espera
                                    llegada=self.cuenta
                                for g in self.cola:
                                         if g.llegada==False:
                                              g.tiempo_llegada=self.cuenta
                                              g.llegada=True
                            if self.acomodar == True: #acomodar es interrumpir y se mete a bloqueo
                                self.acomodar = False
                                i.eta=i.eta-i.contador
                                self.bloqueados.append(i)
                                flag=False

                            
                            if flag == False:
                                flag= True
                                break
                            if self.descartar == True: #agregar a terminados por ERRORR 
                                self.descartar = False
                                self.listaDeTerminados.append(i)
                                i.oper=10
                                i.eta=i.contador
                                if len(self.listaDeProcesos)!=0:
                                    self.cola.append(self.listaDeProcesos[0])
                                    self.listaDeProcesos.popleft()
                                    llegada=self.cuenta
                                for g in self.cola:
                                         if g.llegada==False:
                                              g.tiempo_llegada=self.cuenta
                                              g.llegada=True
                                break
                            
                            
                            if self.pausa == True:
                                pausa = msvcrt.getch()
                                while (pausa != b'c'):
                                    pausa = msvcrt.getch()
                                self.pausa = False
                        self.terminados()  
                        i.tiempo_espera=self.cuenta
          return              
    
    
    def terminados(self):
        print("Terminados\n//////////\n")
        for i in self.listaDeTerminados:
            if(i.oper ==1):
                print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==2):
                print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==3):
                print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==4):
                print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==5):
                print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==6):
                print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==10):
                print("ID   " ,i.id, "ERROR" )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_llegada+i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
        #self.total=self.total-1

                             
                
                    