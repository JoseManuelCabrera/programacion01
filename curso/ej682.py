Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> palabra = "separar"
>>> caracter = ","
>>> for letra in palabra:
	re
KeyboardInterrupt
>>> resultado = ""
>>> for letra in palabra:
	resultado = resultado + letra + caracter

	
>>> resultado
's,e,p,a,r,a,r,'
>>> resultado = resultado[:-1]
>>> resultado
's,e,p,a,r,a,r'
>>> for letra in palabra:
	print(letra)

	
s
e
p
a
r
a
r
>>> palabra.split()
['separar']
>>> palabra.strip()
'separar'
>>> clear
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cadena = "mi archivo de texto.txt"
>>> cadena.replace(" ", "_")
'mi_archivo_de_texto.txt'
>>> 
>>> 
>>> 
>>> cad = "su clave es: 1540"
>>> nueva = ""
>>> for letra in cad:
	if letra.isdigit():
		nueva = nueva + "X"
	else:
		nueva = nueva + letra

		
>>> nueva
'su clave es: XXXX'
>>> pal = "milanesa"
>>> pal[0]
'm'
>>> pal[4]
'n'
>>> pal[1:3]
'il'
>>> pal[1:]
'ilanesa'
>>> 
