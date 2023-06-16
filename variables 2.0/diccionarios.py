#creacion de diccionario con dict
diccionario = dict(nombre ="lucas", apellido = "dalto")# de esta forma se pueden crear diccionarios vacios, de la forma convencional no

#las listas no pueden ser claves
diccionario1 = {('dalto','rancio'):"jajajaj"}#Con tuplas se puede, con listas no, a menos que se use el frozenset

#crear diccionarios con fromkeys, funcion que poermite crear un diccionario con valores:none
diccionario2 = dict.fromkeys(["nombre", "apellido"])#itera el primer elemento por eso muestra cada letra de "nombre" con el valor apellido, a menos que el valor ingresado sea una lista

