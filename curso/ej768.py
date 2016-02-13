#!/usr/bin/env python3
# coding: utf-8

# Ejercicio 7.6.8. Inversión de listas
#     a) Realizar una función que, dada una lista, devuelva una nueva lista
#     cuyo contenido sea igual a la original pero invertida. Así, dada la lista 
#     [’Di’, ’buen’, ’día’, ’a’, ’papa’], deberá devolver
#     [’papa’, ’a’, ’día’, ’buen’, ’Di’].
#     b) Realizar otra función que invierta la lista, pero en lugar de devolver 
#     una nueva, modifique la lista dada para invertirla, si usar listas
#     auxiliares.

def inversor(lista):
    aux = []

    for item in reversed(lista):
        aux.append(item)

    return aux

def inversor2(lista):
    lista.reverse()


if __name__ == "__main__":
    lst = ['Di', 'buen', 'día', 'a', 'papa']
    print(inversor(lst))
    inversor2(lst)
    print(lst)
