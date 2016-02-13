#!/usr/bin/env python3

# Ejercicio 7.6.2. Dominó.
#     a) Escribir una función que indique si dos fichas de dominó encajan o no. 
#     Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
#     b) Escribir una función que indique si dos fichas de dominó encajan o no. 
#     Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
#     Nota: utilizar la función split de las cadenas.

def domino_tuplas(ficha1, ficha2):
    for numero in ficha1:
        if numero in ficha2:
            return True
    return False

def dominio_str(fichas):
    lista_fichas = fichas.split()
    return dominio_strings(lista_fichas[0], lista_fichas[1])

def domino_strings(ficha1, ficha2):
    f1 = ficha1.split("-")
    f2 = ficha2.split("-")
    return domino_tuplas(f1, f2)

f1 = (1, 0)
f2 = (2, 3)
f3 = (0, 3)

print(domino_tuplas(f1, f2)) # False
print(domino_tuplas(f1, f3)) # True
print(domino_tuplas(f2, f1)) # False
print(domino_tuplas(f2, f3)) # True
print(domino_tuplas(f3, f1)) # True
print(domino_tuplas(f3, f2)) # True

f4 = "5-6"
f5 = "1-2"
f6 = "2-6"

print(domino_strings(f4, f5)) # False
print(domino_strings(f4, f6)) # True
print(domino_strings(f5, f4)) # False
print(domino_strings(f5, f6)) # True
print(domino_strings(f6, f4)) # True
print(domino_strings(f6, f5)) # True
