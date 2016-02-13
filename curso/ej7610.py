#!/usr/bin/env python3
# coding: utf-8

# Ejercicio 7.6.10. Matrices.
#     a) Escribir una función que reciba dos matrices y devuelva la suma.
#     b) Escribir una función que reciba dos matrices y devuelva el producto.
#     c) Escribir una función que opere sobre una matriz y mediante eliminación 
#     gaussiana devuelva una matriz triangular superior.
#     d) Escribir una función que indique si un grupo de vectores, recibidos
#     mediante una lista, son linealmente independientes o no.

def suma_matrices(mat1, mat2):
    suma = [[0 for x in len(mat1)] for y in len(mat1[0])]
    for i in range(mat1):
        for j in range(mat1[i]):
            suma[i][j] = mat1[i][j] + mat2[i][j]
    return suma

if __name__ == "__main__":
    m1 = [[1,2,3], [4,5,6], [7,8,9]]
    m2 = [[1,1,1], [1,1,1], [1,1,1]]

    print(suma_matrices(m1, m2))
