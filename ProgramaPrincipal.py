import msvcrt 
import threading
from collections import deque

from Prueba import *

def prueba():
    prueba = Prueba()
    threading.Thread(name="Hilo1", target=esperar, args=(prueba, )).start()

    prueba.prueba()

def esperar(prueba):
    while(True):
        teclado = msvcrt.getch()
        if (teclado == b'e'):
            prueba.doDescartar()
            
        if (teclado == b'i'):
            prueba.doAcomodar()

        if (teclado == b'p'):
            prueba.doPausa()



prueba()