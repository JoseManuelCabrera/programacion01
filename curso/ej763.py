#!/usr/bin/env python3

# Ejercicio 7.6.3. Campaña electoral
#     a) Escribir una función que reciba una tupla con nombres, y para cada
#     nombre imprima el mensaje Estimado <nombre>, vote por mí.
#     b) Escribir una función que reciba una tupla con nombres, una posición de 
#     origen p y una cantidad n, e imprima el mensaje anterior para los n
#     nombres que se encuentran a partir de la posición p.
#     c) Modificar las funciones anteriores para que tengan en cuenta el género 
#     del destinatario, para ello, deberán recibir una tupla de tuplas,
#     conteniendo el nombre y el género.

def votenxmi(tupla):
    for nombre in tupla:
        print("Estimado {}, vote por mí!".format(nombre))

def votenxmi2(tupla, origen, cantidad):
    nueva = tupla[origen:origen + cantidad]
    votenxmi(nueva)

def votenxmi3(tupla, origen, cantidad):
    nueva = tupla[origen:origen + cantidad]
    for persona in nueva:
        if persona[1] == "f":
            print("Estimada {}, vote por mí!".format(persona[0]))
        else:
            print("Estimado {}, vote por mí!".format(persona[0]))

nombres = ("juan", "pedro", "camila", "florencia", "esteban", "micaela")
padron = (("juan", "m"), ("pedro", "m"), ("camila", "f"), ("florencia", "f"), ("esteban", "m"),  ("micaela", "f"))

votenxmi(nombres)
print("="*5)
votenxmi2(nombres, 2, 3)
print("="*5)
votenxmi3(padron, 0, 6)

