#!/usr/bin/env python3

# Eercicio 7.6.6. 
# Dada una lista de números enteros y un entero k, escribir una función que:
#     a) Devuelva tres listas, una con los menores, otra con los mayores y otra
#     con los iguales a k.
#     b) Devuelva una lista con aquellos que son múltiplos de k.

def tres_listas(lista, k):
    menores = []
    mayores = []
    iguales = []
    for numero in lista:
        if numero > k:
            mayores.append(numero)
        elif numero < k:
            menores.append(numero)
        else:
            iguales.append(numero)
    return mayores, menores, iguales

lista1 = [10, 20, 34, 56, 8, -3, 123, 20, 17, 20, 58, -1]

print(tres_listas(lista1, 20))
