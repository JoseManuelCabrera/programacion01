#!/usr/bin/env python3
# coding: utf-8

# Ejercicio 7.6.9.
#     Escribir una función empaquetar para una lista, donde empaquetar
#     significa indicar la repetición de valores consecutivos mediante una
#     tupla (valor, cantidad de repeticiones). Por ejemplo,
#     empaquetar([1,1,1,3,5,1,1,3,3]) debe devolver
#     [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].

def contar_apariciones_seguidas(lista, index=0):
    """Cuenta las ocurrencias seguidas del primer elemento de la lista y
    devuelve una tupla con la cantidad de apariciones de ese elemento y el
    índice de la lista en el que terminan las apariciones.

    Por ejemplo:

        [1,2,1,1,1,2,3] --> (1, 0)

        [3,3,3,4] --------> (3, 2)
    """
    apariciones = 1
    index = index
    while index+1 < len(lista) and lista[index] == lista[index+1]:
        apariciones += 1
        index += 1
    return (apariciones, index)

def empaquetar(lista):
    index = -1
    paquetes = []
    while index+1 < len(lista):
        apariciones, index = contar_apariciones_seguidas(lista, index+1)
        paquete = (lista[index], apariciones)
        paquetes.append(paquete)
    return paquetes

if __name__ == "__main__":
    lst = [1, 1, 1, 3, 5, 1, 1, 3, 3]
    print(empaquetar(lst))
