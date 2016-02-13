#!/usr/bin/env python3

# Ejercicio 7.6.1. 
#     Escribir una función que reciba una tupla de elementos e indique si se 
#     encuentran ordenados de menor a mayor o no.

def tupla_ordenada(tupla):
    ordenada = sorted(tupla, reverse=True)
    for item in tupla:
        if item != ordenada.pop():
            return False
    return True

if __name__ == "__main__":
    print("Vamos a probar la función:")
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("1° Tupla: {}".format(tupla1))
    if tupla_ordenada(tupla1):
        print("La Tupla está en orden!")
    else:
        print("La Tupla no está en orden!")

    tupla2 = (1, 20, 3, 4, 50, 6, 7, 8, 9, 10)
    print("2° Tupla: {}".format(tupla2))
    if tupla_ordenada(tupla2):
        print("La Tupla está en orden!")
    else:
        print("La Tupla no está en orden!")
