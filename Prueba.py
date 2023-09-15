import time 
from collections import deque

class Prueba:
    descartar = False

    def prueba(self):
        cola = deque()
        for i in range(50):
            cola.append(i)
            
        for i in cola:    
            print("Voy en la ", i)
            
            for i in range(10):
                if self.descartar == True:
                    self.descartar = False
                    break

                time.sleep(1)

    def  doDescartar(self):
        self.descartar = True
