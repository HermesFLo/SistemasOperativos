import msvcrt 
import threading
from collections import deque
from Prueba import Prueba

def prueba():
    prueba = Prueba()
    threading.Thread(name="Hilo1", target=esperar, args=(prueba, )).start()

    prueba.prueba()

def esperar(prueba):
    while(True):
        teclado = msvcrt.getch()
        if (teclado == b'e'):
            print(teclado)
            prueba.doDescartar()

prueba()