#!/usr/bin/env python3
# conding: utf-8

# Ejercicio 5.7.3. Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le
# pregunte al usua- rio la contraseña, y no le permita continuar hasta que la
# haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad
# fija de intentos.
# c) Modificar el programa anterior para que después de cada intento agregue
# una pausa cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el
# usuario ingresó o no la contraseña correctamente, mediante un valor booleano
# (True o False).

import time

PASSWORD = 'contraseña'
INTENTOS = 3

def confirmar_passwd():
    confirmado = False
    while not confirmado:
        passwd = input("Ingrese su contraseña: ")
        if passwd == PASSWORD:
            confirmado = True
            print("Contraseña verificada!")
        else:
            print("Contraseña incorrecta!")

    print("Chau chau chau...")

def confirmar_passwd2():
    intentos = 0
    confirmado = False
    while not confirmado and intentos < INTENTOS:
        passwd = input("Ingrese su contraseña: ")
        intentos = intentos + 1
        if passwd == PASSWORD:
            confirmado = True
            print("Contraseña verificada!")
        else:
            print("Contraseña incorrecta!")

    print("Chau chau chau...")

def confirmar_passwd3():
    intentos = 0
    confirmado = False
    while not confirmado and intentos < INTENTOS:
        passwd = input("Ingrese su contraseña: ")
        intentos = intentos + 1
        if passwd == PASSWORD:
            confirmado = True
            print("Contraseña verificada!")
        else:
            tiempo = intentos + 1
            time.sleep(tiempo)
            print("Contraseña incorrecta!")

    print("Chau chau chau...")

def confirmar_passwd4():
    intentos = 0
    confirmado = False
    while not confirmado and intentos < INTENTOS:
        passwd = input("Ingrese su contraseña: ")
        intentos = intentos + 1
        if passwd == PASSWORD:
            confirmado = True
            print("Contraseña verificada!")
            return True
        else:
            tiempo = intentos + 1
            time.sleep(tiempo)
            print("Contraseña incorrecta!")

    print("Chau chau chau...")
    return False

#confirmar_passwd()
#confirmar_passwd2()
#confirmar_passwd3()
if confirmar_passwd4():
    print("Hola usuario!!! Te extrañe...")
else:
    print("Salí de acá, impostor!!!")
