Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> lista = [1, 2, "Leandro", "Emilia", 3, 4, "Sofía"]
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Sofía']
>>> lista2 = [0, 1, lista]
>>> lista2
[0, 1, [1, 2, 'Leandro', 'Emilia', 3, 4, 'Sofía']]
>>> type(lista)
<class 'list'>
>>> len(lista)
7
>>> lista[0]
1
>>> lista[-1]
'Sofía'
>>> lista[-1] = "Casa Sofía Yussen"
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Casa Sofía Yussen']
>>> lista[6]
'Casa Sofía Yussen'
>>> lista[7]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lista[7]
IndexError: list index out of range
>>> lista[7] = "Jean"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    lista[7] = "Jean"
IndexError: list assignment index out of range
>>> lista.append("Jean")
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Casa Sofía Yussen', 'Jean']
>>> len(lista)
8
>>> lista[7] = "Jean Pool"
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Casa Sofía Yussen', 'Jean Pool']
>>> lista3 = [10, 34, 4, 6, 8, 21, -3, 5]
>>> lista3
[10, 34, 4, 6, 8, 21, -3, 5]
>>> lista.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lista.sort()
TypeError: unorderable types: str() < int()
>>> 
>>> lista3.sort()
>>> lista3
[-3, 4, 5, 6, 8, 10, 21, 34]
>>> lista4 = ["frutilla", "anana", "durazno", "pera"]
>>> lista4.sort()
>>> lista4
['anana', 'durazno', 'frutilla', 'pera']
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Casa Sofía Yussen', 'Jean Pool']
>>> lista.pop()
'Jean Pool'
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4, 'Casa Sofía Yussen']
>>> lista.pop()
'Casa Sofía Yussen'
>>> lista
[1, 2, 'Leandro', 'Emilia', 3, 4]
>>> lista.count()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lista.count()
TypeError: count() takes exactly one argument (0 given)
>>> 
>>> 
>>> lista.remove("Leandro")
>>> lista
[1, 2, 'Emilia', 3, 4]
>>> lista.index("Emilia")
2
>>> lista[2]
'Emilia'
>>> lista4
['anana', 'durazno', 'frutilla', 'pera']
>>> "anana" in lista4
True
>>> "papa" in lista4
False
>>> 1 in lista
True
>>> 5 in lista
False
>>> tupla1 = (1, 5, "Leo", "sofia")
>>> tupla1
(1, 5, 'Leo', 'sofia')
>>> len(tupla1)
4
>>> tupla1.index(5)
1
>>> tupla1.index(1)
0
>>> tupla1.index(6)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    tupla1.index(6)
ValueError: tuple.index(x): x not in tuple
>>> tupla1[3] = "Sofía"
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    tupla1[3] = "Sofía"
TypeError: 'tuple' object does not support item assignment
>>> diccionario = {"nombre": "Leandro", "apellido": "Colombo Viña", "edad": 34}
>>> diccionario
{'edad': 34, 'apellido': 'Colombo Viña', 'nombre': 'Leandro'}
>>> len(diccionario)
3
>>> diccionario.keys()
dict_keys(['edad', 'apellido', 'nombre'])
>>> diccionario['nombre']
'Leandro'
>>> diccionario['edad']
34
>>> diccionario['edad'] += 1
>>> diccionario['edad']
35
>>> diccionario['nombre'] = "Leandro Enrique"
>>> diccionario['nombre']
'Leandro Enrique'
>>> diccionario['dni'] = 29076668
>>> diccionario['dni']
29076668
>>> diccionario
{'edad': 35, 'apellido': 'Colombo Viña', 'dni': 29076668, 'nombre': 'Leandro Enrique'}
>>> diccionario['familia'] = ["Mama", "Papa", "Hijo", "Esposa"]
>>> diccionario
{'edad': 35, 'apellido': 'Colombo Viña', 'familia': ['Mama', 'Papa', 'Hijo', 'Esposa'], 'dni': 29076668, 'nombre': 'Leandro Enrique'}
>>> diccionario['familia']
['Mama', 'Papa', 'Hijo', 'Esposa']
>>> type(diccionario['familia'])
<class 'list'>
>>> diccionario['familia'].append("Abuela")
>>> diccionario['familia']
['Mama', 'Papa', 'Hijo', 'Esposa', 'Abuela']
>>> diccionario2 = {'clave': diccionario}
>>> diccionario2['clave']
{'edad': 35, 'apellido': 'Colombo Viña', 'familia': ['Mama', 'Papa', 'Hijo', 'Esposa', 'Abuela'], 'dni': 29076668, 'nombre': 'Leandro Enrique'}
>>> diccionario
{'edad': 35, 'apellido': 'Colombo Viña', 'familia': ['Mama', 'Papa', 'Hijo', 'Esposa', 'Abuela'], 'dni': 29076668, 'nombre': 'Leandro Enrique'}
>>> 
