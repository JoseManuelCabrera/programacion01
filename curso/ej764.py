#!/usr/bin/env python3

# Ejercicio 7.6.4. Vectores
#     a) Escribir una función que reciba dos vectores y devuelva su producto
#     escalar.
#     b) Escribir una función que reciba dos vectores y devuelva si son o no
#     ortogonales.
#     c) Escribir una función que reciba dos vectores y devuelva si son
#     paralelos o no.
#     d) Escribir una función que reciba un vector y devuelva su norma.

def producto_escalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return False
    return sum(p*q for p,q in zip(vector1, vector2)

def son_ortogonales(vector1, vector2):
    return producto_escalar(vector1, vector2) == 0

def son_paralelos(vector1, vector2):
    lista = []
    for item in zip(vector1, vector2):
        lista.append(item[0]/item[1])
    return set(lista) == 1

def norma(vector):
    return sum(x**2 for x in vector)**0.5

