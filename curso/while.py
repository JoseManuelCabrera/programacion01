#!/usr/bin/env python3
# coding: utf-8

def analizar_numero():
    x = int(input("Ingrese un número: "))
    if x > 0:
        print("El número es POSITIVO!")
    elif x < 0:
        print("El número es NEGATIVO!")
    else:
        print("Ingresaste CERO, picarón!")

def preguntar_veces():
    n = int(input("¿Cuántos números vas a analizar?"))
    for i in range(n):
        analizar_numero()
    print("Gracias por usarme!")

def desea_continuar():
    continuar = True
    while continuar == True:
        analizar_numero()
        rta = input("¿Desea continuar? ")
        if rta == "No":
            continuar = False
    print("Gracias por usarme!")


#analizar_numero()
#preguntar_veces()
desea_continuar()
