#!/usr/bin/env python3
# coding: utf-8

# El programa debe pedir tres duraciones expresadas en horas,
# minutos y segundos, y las tiene que mostrar en pantalla
# expresadas en segundos.

# Definimos la función
def conversor():
    """Va a pedir el tiempo en horas, minutos y segundos y va a
       devolver la cantidad total de segundos."""

    # Entrada de Datos
    horas = input("Ingrese la cantidad de horas: ")
    minutos = input("Ingrese la cantidad de minutos: ")
    segundos = input("Ingrese la cantidad de segundos: ")

    # Proceso de esos datos
    seguntos_totales = 3600 * float(horas) + 60 * float(minutos) + float(segundos)

    # Salida de Datos
    print("Equivale a {} segundos".format(seguntos_totales))

# Ejecutamos la función recientemente definida.
conversor()
conversor()
