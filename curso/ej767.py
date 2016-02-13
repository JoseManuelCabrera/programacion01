#!/usr/bin/env python3
# coding: utf-8

# Ejercicio 7.6.7.
#     Escribir una función que reciba una lista de tuplas (Apellido, Nombre,
#     Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una
#     contenga primero el nombre, luego la inicial con un punto, y luego el
#     apellido.

def componer_nombre(lista_tuplas):
    lista_nombres = []

    for tupla in lista_tuplas:
        nombre_completo = "{} {}. {}".format(tupla[1], tupla[2], tupla[0])
        lista_nombres.append(nombre_completo)

    return lista_nombres

if __name__ == "__main__":
    n1 = ("Perón", "Juan", "D")
    n2 = ("Alfonsín", "Raúl", "R")
    n3 = ("Fangio", "Juan", "M")
    n4 = ("Maradona", "Diego", "A")
    lst = [n1, n2, n3, n4]

    for item in componer_nombre(lst):
        print(item)

