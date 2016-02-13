#!/usr/bin/env python
# coding: utf-8

# Ejercicio 4.1. El usuario del tarifador nos pide ahora una modificación, ya que no es lo mismo
# la tarifa por segundo de las llamadas cortas que la tarifa por segundo de las llamadas largas.
# Al inicio del programa se informará la duración máxima de una llamada corta, la tarifa de las
# llamadas cortas y la de las largas. Se deberá facturar con alguno de los dos valores de acuerdo
# a la duración de la comunicación.

def main():
    """ El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo. """

    print("Las llamadas cortas duran menos de 10 minutos.")
    tl = float(input("¿Cuánto cuesta 1 segundo de comunicacion larga?: "))
    tc = float(input("¿Cuánto cuesta 1 segundo de comunicacion corta?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))

    for x in range(n):
        hs = int(input("¿Cuántas horas?: "))
        min = int(input("¿Cuántos minutos?: "))
        seg = int(input("¿Cuántos segundos?: "))
        segcalc = asegundos(hs, min, seg)
        # Si la llamada es de más de 600 segundos, cobramos con la tarifa de
        # llamada larga. Sino, cobramos con la tarifa de llamada corta.
        if segcalc > 600:
            costo = segcalc * tl
        else:
            costo = segcalc * tc
        print("Duracion: ", segcalc, "segundos. Costo: ",costo, "$.")

def asegundos(horas, minutos, segundos):
    """ Convierte horas, minutos y segundos a su valor
    equivalente en segundos.
    """
    segsal = 3600 * horas + 60 * minutos + segundos

    return segsal

main()
