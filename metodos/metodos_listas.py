#creando uns lista con list()
lista = list([34,56,23,True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista) #4

#agregando elemento con append
lista.append(64)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"toma mama")#el primer valor es el indice y el segundo el valorde lo que se ingresa

#agregando varios elementos a la lista
lista.extend([False, 2030])# se agregan al final

#eliminando un elemento de la lista por su indice
lista.pop(3)#-1 para eliminar el ultimo -2 para el anteultimo y asi sicesivamente

#remover un elemento de la lista (por su valor)
lista.remove("toma mama")

#ordena la lista (si se usa el parametro reverse=True, lo ordena en reversa)
lista.sort()#no funciona con cadenas de texto, y los false van antes de los true, reverse=True, invierte los elementos

#invirtiendo los elemntos de una lista
lista.reverse()