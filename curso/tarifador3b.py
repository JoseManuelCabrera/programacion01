#!/usr/bin/env python3
# coding: utf-8

# Ejercicio 4.1. El usuario del tarifador nos pide ahora una modificación, ya
# que no es lo mismo la tarifa por segundo de las llamadas cortas que la tarifa
# por segundo de las llamadas largas.
# Al inicio del programa se informará la duración máxima de una llamada corta,
# la tarifa de las llamadas cortas y la de las largas. Se deberá facturar con
# alguno de los dos valores de acuerdo a la duración de la comunicación.

# Ejercicio 4.2. Mantenimiento del tarifador:
# a) Al nuevo programa que cuenta con llamadas cortas y largas, agregarle los
#    adicionales, de modo que:
#       - Los montos se escriban como pesos y centavos.
#       - Se informe además cuál fue el total facturado en la corrida.
# b) Modificar el programa para que sólo informe cantidad de llamadas cortas,
# valor total de llamadas cortas facturadas, cantidad de llamadas largas, valor
# total de llamadas largas facturadas, y total facturado. Al llegar a este
# punto debería ser evidente que es conveniente separar los cálculos en
# funciones aparte.

def main():
    """ El usuario ingresa la tarifa por segundo, cuántas comunicaciones se
    realizaron, y la duracion de cada comunicación expresada en horas, minutos
    y segundos. Como resultado se informa la duración en segundos de cada
    comunicación y su costo. """

    print("Las llamadas cortas duran menos de 10 minutos.")
    tl = float(input("¿Cuánto cuesta 1 segundo de comunicacion larga?: "))
    tc = float(input("¿Cuánto cuesta 1 segundo de comunicacion corta?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))

    costo_total_largas = 0
    costo_total_cortas = 0
    cant_largas = 0
    cant_cortas = 0
    for x in range(n):
        print("Ingrese el la duración de la llamada N°{}:".format(x + 1))
        hs = int(input("¿Cuántas horas?: "))
        min = int(input("¿Cuántos minutos?: "))
        seg = int(input("¿Cuántos segundos?: "))
        segcalc = asegundos(hs, min, seg)
        # Si la llamada es de más de 600 segundos, cobramos con la tarifa de
        # llamada larga. Sino, cobramos con la tarifa de llamada corta.
        if segcalc > 600:
            costo = costo_llamadas(tl, segcalc)
            costo_total_largas = costo_total_largas + costo
            cant_largas = cant_largas + 1
        else:
            costo = costo_llamadas(tc, segcalc)
            costo_total_cortas = costo_total_cortas + costo
            cant_cortas = cant_cortas + 1

    print()
    print("="*80)
    imprimir_cantidad_y_costos('cortas', cant_cortas, costo_total_cortas)
    imprimir_cantidad_y_costos('largas', cant_largas, costo_total_largas)
    print("-"*80)

    costo_total = costo_total_largas + costo_total_cortas
    print("Costo total: ${:.2f}".format(costo_total))
    print("="*80)
    print()

def asegundos(horas, minutos, segundos):
    """ Convierte horas, minutos y segundos a su valor
    equivalente en segundos.
    """
    segsal = 3600 * horas + 60 * minutos + segundos

    return segsal

def costo_llamadas(tarifa, duracion):
    """ Recibe una duracion en segundos y la tarifa en pesos y devuelve el
    costo de la llamada.
    """
    costo = tarifa * duracion

    return costo

def imprimir_cantidad_y_costos(tipo, cantidad, costo):
    """ Recibe el tipo de llamada, la cantidad y el costo e imprime estos
    valores."""

    msg = """Cantidad de llamadas {0}: {1}
    Costo llamadas {0}: ${2:.2f}""".format(tipo, cantidad, costo)

    print(msg)

main()
