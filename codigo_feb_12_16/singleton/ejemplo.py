# -*- coding: cp1252 -*-
import time

def singleton(refresh=False):
    
    if refresh:
        singleton.instancia=""
    
    # Si ya esta creado lo retornamos:
    if singleton.instancia:
        return singleton.instancia

    # Asignar tiempo a la variable:
    singleton.instancia = str(time.strftime("%H:%M:%S"))
    print("Singleton creado")    
    return singleton.instancia

# Asocia un atributo a una funcion
singleton.instancia=""


print("Sin refresco, siempre la misma hora")
print(singleton())
time.sleep(1)
print("siguiente llamada")
print(singleton())
print()
print("Con refresco, cada llamada cambia la hora")
print(singleton(True))
time.sleep(1)
print(singleton(True))




