#!/usr/bin/env python
# coding: utf-8

# Problema 3.1. Un usuario nos plantea su problema: necesita que se facture el
# uso de un teléfono.
# Nos informará la tarifa por segundo, cuántas comunicaciones se realizaron, la duración
# de cada comunicación expresada en horas, minutos y segundos. Como resultado deberemos
# informar la duración en segundos de cada comunicación y su costo.

def main():
    """ El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo. """

    f = float(input("¿Cuánto cuesta 1 segundo de comunicacion?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))

    for x in range(n):
        hs = int(input("¿Cuántas horas?: "))
        min = int(input("¿Cuántos minutos?: "))
        seg = int(input("¿Cuántos segundos?: "))
        segcalc = asegundos(hs, min, seg)
        costo = segcalc * f
        print("Duracion: ", segcalc, "segundos. Costo: ",costo, "$.")

def asegundos(horas, minutos, segundos):
    """ Convierte horas, minutos y segundos a su valor
    equivalente en segundos.
    """
    segsal = 3600 * horas + 60 * minutos + segundos

    return segsal

main()
