from Proceso import *
from random import *
from collections import deque
import msvcrt 
import time 
import os
import threading
global opc, contador_gen ,cuenta 
def Captura():
        listaDeProcesos=deque()
        contador_gen = 0
        opc = int(input("Numero de registros "))
        for i in range(opc):
            proceso=Proceso()
            proceso.oper =randrange(1,7)
            proceso.n1 = randrange(1,100)
            proceso.n2= randrange(1,100)
            operaciones(proceso)
            proceso.eta=randrange(1,6)
            contador_gen=contador_gen+ proceso.eta 
            proceso.id= "N" + str(i+1)
            listaDeProcesos.append(proceso)
            t1= threading.Thread(name="Hilo1", target=imprimir, args=(listaDeProcesos, ))
            
        imprimir(listaDeProcesos)
        t1.start()

def operaciones(proceso):
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
def contador(contador_gen):
     for z in range(contador_gen):
          print("Contador: ",z)
def teclado(cola1,i,listaDeTerminados,cola):
     ch = msvcrt.getch()
     if (ch == b'i'):
        print("Soy interrupcion")
        cola1.append(i)
        cola1.popleft()
        return 
     if (ch == b'e'):
        print("Soy error")
        cola1.popleft()
        listaDeTerminados.append(i)
        return cola1 ,i,listaDeTerminados
     if (ch == b'p'):
          os.wait()
          ch = msvcrt.getch()
          #if(ch == b'c'):   

def imprimir(listaDeProcesos):
     listaDeTerminados=[]
     cola=deque()
     cola1=deque()
     total=len(listaDeProcesos)
     while(len(listaDeProcesos) > 0): #acabar los elementos de la lista
        cola.clear()
        cola1.clear()
        for a in range(5):#añadir lote a la cola 
              cola.append(listaDeProcesos[0])
              cola1.append(listaDeProcesos[0])
              listaDeProcesos.popleft()
              cuenta = 0
              if(len(listaDeProcesos) == 0):#termina si la listadeprocesos tiene un lote sin llenar 
                    break
        
        for i in cola:
                t2= threading.Thread(name="Hilo2", target=teclado, args=(cola1,i,listaDeTerminados,cola))
                t2.start()
                if(total==5 or total==10 or total==15):
                     print("No. Lotes pendientes \n" ,(total//5)-1 )
                print("No. Lotes pendientes \n" ,total//5 )
                print("Pendientes ")
                if(len(cola1)!=0):
                     cola1.popleft()
                for p in cola1:
                    print("ID ",p.id, "Time" ,p.eta,"\n") #imprime los pendientes 

                print("Actual")
                
                for contador in range(i.eta):#proceso en ejecucion + contado AQUI VA LA INTERRUPCION DEL TECLADO
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
                    print("Tiempo total  " ,i.eta , "   Tiempo Transcurrido  " , contador , "   Tiempo Restante  " ,i.eta - contador, "Contador", cuenta)
                    time.sleep(1)
                    
                listaDeTerminados.append(i)
                cuenta=cuenta 
                print("Terminados")
                for i in listaDeTerminados:
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
                total=total-1
                
Captura()
#falta que i quité y ponga en la cola original
#que e elimine y que no se imprima doble en lista de terminados 
#falta que se pause y se continué el programa
