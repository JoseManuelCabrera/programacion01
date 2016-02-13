#!/usr/bin/env python3

def dos_primeros(cadena):
    print(cadena[:2])

def ultimos_tres(cadena):
    print(cadena[-3:])

def cada_dos(cadena):
    print(cadena[::2])

def inverso(cadena):
    print(cadena[::-1])

def reflejo(cadena):
    print(cadena+cadena[::-1])

if __name__ == '__main__':
    cadena = input("Ingrese una cadena de texto: ")

    print("Estos son los primeros 2 caracteres: ")
    dos_primeros(cadena)

    print("Estos son los úlitmos 3 caracteres: ")
    ultimos_tres(cadena)

    print("Esta es la cadena cada 2 caracteres: ")
    cada_dos(cadena)

    print("Esta es la cadena inversa: ")
    inverso(cadena)

    print("Esta es la cadena reflejada: ")
    reflejo(cadena)

