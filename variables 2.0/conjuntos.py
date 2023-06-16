#creando un conjunto con set
conjunto = set(["Dato 1", "Dato 2"]) #se le pasa una lista

#metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset (['dato 1', 'dato 2']) #crea un conjunto inmutable para que sea hasheable
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#teoria de conjuntos

conjunto3 = {1, 3, 5, 7}
conjunto4 = {1, 3, 7}

resultado1 = conjunto4.issubset(conjunto3)# pregunta si el conjunto 4 es un subconjunto de conjunto 3, da true
resultado2 = conjunto4 <= conjunto3 #es lo mismo
resultado3 = conjunto3 > conjunto4 #pregunta si el conjunto 3 es superconjunto de conjunto 4

#verificar si hay resultados en comun
resultado4 = conjunto4.isdisjoint(conjunto3)# va a ser true solo si los elementos que se comparan no tienen elementos en comun

