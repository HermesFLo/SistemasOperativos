class Proceso:
    
    id = str()
    oper=str()
    n1=int()
    n2=int()
    eta=int()
    res=int()
    bloqueo=0
    tiempo_llegada=0
    tiempo_final=int()
    tiempo_espera=int()
    tiempo_respuesta=tiempo_llegada+tiempo_espera
    tiempo_retorno=tiempo_final - tiempo_llegada
    tiempo_servicio=tiempo_respuesta-tiempo_espera
    contador=0