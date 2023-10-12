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
    anadir=False
    ver= False
    listaDeTerminados=[]
    cola=deque()
    listaDeProcesos=deque()
    cuenta = 0
    detenido=1
    numid=0
    current=deque()
    bloqueados=deque()
    quantum=int() 
    cont_q=1
    interrupters:deque()
    def prueba(self):
        
        contador_gen = 0
        opc = int(input("Numero de registros "))
        qua = int(input("Tiempo de Quantum "))
        self.quantum=qua
        for i in range(opc):
            proceso=Proceso()
            proceso.oper =randrange(1,6)
            proceso.n1 = randrange(1,100)
            proceso.n2= randrange(1,100)
            self.operaciones(proceso)
            proceso.eta=randrange(6,9)
            contador_gen=contador_gen+ proceso.eta 
            proceso.id= "N" + str(self.numid+1)
            self.numid=self.numid+1
            self.listaDeProcesos.append(proceso)
        self.imprimir(self.listaDeProcesos)
    def  doDescartar(self):
        self.descartar = True
    def  doBcp(self):
        self.ver = True
    def  doAgregar(self):
        self.anadir = True
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
          rango=range(len(self.cola))
          flag= True
          llegada=0
          #for p in range(len(self.cola)):
          while (len(self.cola) >0 or len(self.bloqueados) >0): #esto es lo principaaaaaaaaaaal
            if len(self.cola) == 0:
                 time.sleep(1)
                 self.unomasbloq()
                 continue 
            total=len(self.listaDeProcesos)
        
            if len(self.cola) >0:
                i=self.cola.popleft()
            print("No. Procesos nuevos  \n" , total)
            print("Nuevos"   ,"Valor del Quantum  ",self.quantum )
            if len(self.cola) >0:
                for a in self.cola:
                    print("ID ",a.id, "Time" ,a.eta,"Tiempo Transcurrido",a.contador,"\n") #imprime los pendientes """
                    #a.tiempo_llegada=self.cuenta
            
            self.terminados()

            print("Actual")
            espera=self.cuenta
            for i.contador in range(i.eta):#proceso en ejecucion + contado AQUI VA LA INTERRUPCION DEL TECLADO
                self.cuenta=self.cuenta + 1
                i.tiempo_espera=self.cuenta+1
                if(i.oper ==1):
                    print("ID ", i.id, " Ope  ", i.n1," + ",i.n2,"Quantum: ",self.cont_q,"\n")
                if(i.oper ==2):
                    print("ID ", i.id, " Ope  ", i.n1," - ",i.n2,"Quantum: ",self.cont_q,"\n") 
                if(i.oper ==3):
                    print("ID ", i.id,  " Ope  ", i.n1," * ",i.n2,"Quantum: ",self.cont_q,"\n") 
                if(i.oper ==4):
                    print("ID ", i.id,  " Ope  ", i.n1," / ",i.n2,"Quantum: ",self.cont_q,"\n")
                if(i.oper ==5):
                    print("ID ", i.id, " Ope  ", i.n1," // ",i.n2,"Quantum: ",self.cont_q,"\n")
                if(i.oper ==6):
                    print("ID ", i.id,  "Ope ", i.n1," % ",i.n2, "Quantum: ",self.cont_q ,"\n")
                print("Tiempo total  " ,i.eta , "   Tiempo Transcurrido  " , i.contador , "   Tiempo Restante  " ,i.eta - i.contador, "Contador", self.cuenta)
                self.cont_q=self.cont_q+1
                time.sleep(2)
                
                
                if i.contador == i.eta-1:#aregar a terminados
                    i.tiempo_final=self.cuenta
                    self.listaDeTerminados.append(i)
                    i.eta=i.contador
                    self.cont_q=1
                    if len(self.listaDeProcesos)!=0 and (len(self.cola) + len(self.bloqueados) <5):
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
                    self.cont_q=1   
                    flag=False
                if self.anadir == True: #añade nuevo proceso a donde corresponda
                                 self.anadir= False
                                 if len(self.cola) <4:
                                    proceso=Proceso()
                                    proceso.oper =randrange(1,6)
                                    proceso.n1 = randrange(1,100)
                                    proceso.n2= randrange(1,100)
                                    self.operaciones(proceso)
                                    proceso.eta=randrange(6,9)
                                    proceso.id= "N" + str(self.numid+1)
                                    self.numid=self.numid+1
                                    proceso.tiempo_llegada=self.cuenta
                                    self.cola.append(proceso)
                                    print("//////////////////////////// NUEVO AGREGADO A LISTOS ///////////////////////////////////")
                                    continue
            
                                 if len(self.cola)>=4:
                                    proceso=Proceso()
                                    proceso.oper =randrange(1,6)
                                    proceso.n1 = randrange(1,100)
                                    proceso.n2= randrange(1,100)
                                    self.operaciones(proceso)
                                    proceso.eta=randrange(6,9)
                                    proceso.id= "N" + str(self.numid+1)
                                    self.numid=self.numid+1
                                    self.listaDeProcesos.append(proceso)
                                    print("//////////////////////////// NUEVO AGREGADO A NUEVOS ///////////////////////////////////")
                self.unomasbloq()
                if flag == False:
                    flag= True
                    break
                if self.descartar == True: #agregar a terminados por ERRORR 
                    self.descartar = False
                    i.oper=10
                    i.eta=i.contador
                    i.tiempo_llegada=self.cuenta
                    self.cont_q=1
                    self.listaDeTerminados.append(i)
                    if len(self.listaDeProcesos)!=0 and (len(self.cola) + len(self.bloqueados) <5):
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
                if self.ver == True:
                                pausa = msvcrt.getch()
                                self.current.append(i)
                                self.BCP()
                                while (pausa != b'c'):
                                    pausa = msvcrt.getch()
                                self.ver = False
                                self.current.popleft()    
                                #cambios que hice solo fue agregar tiempo de finalización al meter por error y el tiempo de respuesta es igual al tiempo de espera 
                if self.cont_q==self.quantum+1: #cambio en el quantum
                     i.eta=i.eta-i.contador
                     self.interrupters.append(i)
                     self.cola.append(self.interrupters.popleft())
                     self.cont_q=1
                     
            self.terminados()  
            i.tiempo_espera=self.cuenta
          return              
    def unomasbloq(self):
         if len(self.bloqueados)>0:#Bloqueados
                    for b in self.bloqueados:
                        print("////////////////////////////BLOQUEOOOO///////////////////////////////////")
                        print("ID ",b.id , "Tiempo Bloqueado ",b.tiempo_bloqueado )
                        print("/////////////////////////////////////////////////////////////////////////\n\n")
                        b.tiempo_bloqueado=b.tiempo_bloqueado +1
                        if b.tiempo_bloqueado == 8:#para sacarlo de bloqueo
                            b.bloqueo=b.bloqueo+1
                            b.tiempo_bloqueado= 1
                            self.cola.append(self.bloqueados.popleft())
                            break
    def BCP(self):
         print("\n\n//////////////////////////////////////TABLA BCP//////////////////////////////////////\n\n")
         if len(self.listaDeTerminados)>0:
                for i in self.listaDeTerminados:
                    if(i.oper ==1):
                        print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial " , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==2):
                        print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==3):
                        print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==4):
                        print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==5):
                        print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==6):
                        print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==10):
                        print("ID   " ,i.id, "ERROR" )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")  
         for i in self.current:
            if(i.oper ==1):
                print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial " , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==2):
                print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==3):
                print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==4):
                print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==5):
                print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==6):
                print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==10):
                print("ID   " ,i.id, "ERROR" )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")   
         if len(self.cola)>0:
                for i in self.cola:
                    if(i.oper ==1):
                        print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial " , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==2):
                        print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==3):
                        print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==4):
                        print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==5):
                        print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==6):
                        print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==10):
                        print("ID   " ,i.id, "ERROR" )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
         if len(self.listaDeProcesos)>0:
              for i in self.listaDeProcesos:
                    if(i.oper ==1):
                        print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial " , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==2):
                        print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==3):
                        print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==4):
                        print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==5):
                        print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==6):
                        print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                    if(i.oper ==10):
                        print("ID   " ,i.id, "ERROR" )
                        print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                        print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera Parcial" , (self.cuenta -i.tiempo_llegada)-i.contador , "Tiempo Servicio ",i.eta+1,"\n")
                                  
    def terminados(self):
        print("Terminados\n//////////\n")
        for i in self.listaDeTerminados:
            if(i.oper ==1):
                print("ID   " ,i.id, "Ope   ",i.n1," + ",i.n2, "    Res     ", i.res)
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==2):
                print("ID   " ,i.id, "Ope   ",i.n1," - ",i.n2, "  Res     ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==3):
                print("ID   " ,i.id, "Ope   ",i.n1," * ",i.n2, "  Res   ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==4):
                print("ID   " ,i.id, "Ope   ",i.n1," / ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==5):
                print("ID   " ,i.id, "Ope   ",i.n1," // ",i.n2, " Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==6):
                print("ID   " ,i.id, "Ope   ",i.n1," % ",i.n2, "  Res  ", i.res )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
            if(i.oper ==10):
                print("ID   " ,i.id, "ERROR" )
                print("Tiempo llegada " , i.tiempo_llegada , "Tiempo Finalización " , i.tiempo_final + (i.bloqueo*8), "Tiempo Retorno " ,i.tiempo_final - i.tiempo_llegada)
                print("Tiempo Respuesta " ,i.tiempo_espera,"Tiempo Espera " , i.tiempo_espera , "Tiempo Servicio ",i.eta+1,"\n")
        #self.total=self.total-1

                             
                
                    