#!/usr/bin/env python3

# Ejercicio 7.6.5. Dada una lista de números enteros, escribir una función que:
#     a) Devuelva una lista con todos los que sean primos.
#     b) Devuelva la sumatoria y el promedio de los valores.
#     c) Devuelva una lista con el factorial de cada uno de esos números.

def es_primo(num):
    divisores = 1
    for x in range(1, num):
        if num % x == 0:
            divisores += 1
    return divisores == 2

def primos(lista):
    lista_primos = []
    for num in lista:
        if es_primo(num):
            lista_primos.append(num)
    return lista_primos

def sum_y_prom(lista):
    sumatoria = sum(lista)
    promedio = sumatoria/len(lista)
    return sumatoria, promedio

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def factoriales(lista):
    lista_factoriales = []
    for num in lista:
        lista_factoriales.append(factorial(num))
    return lista_factoriales

print(factoriales([1,2,3,4,5,6]))

