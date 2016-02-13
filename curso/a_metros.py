#!/usr/bin/env python
# coding: utf-8

# 1 milla = 1.609344 km = 1609.344 m
# 1 pie = 30.48 cm = 0.3048 m
# 1 pulgada = 2.54 cm = 0.0254 m

print("Bienvenido!")
print("Este programa sirve para convertir a metros...")
#print("Indique cuántas millas: ")
millas = input("Indique cuántas millas: ")
#print("Indique cuántos pies: ")
pies = input("Indique cuántos pies: ")
#print("Indique cuántas pulgadas: ")
pulgadas = input("Indique cuántas pulgadas: ")

metros = millas * 1609.344 + pies * 0.3048 + pulgadas * 0.0254

resultado = "El total es {} metros".format(metros)
print(resultado)
