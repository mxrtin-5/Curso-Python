animales = ['gato', 'perro','loro','hamster']

for animal in animales: #la variable animal se va a ejecutar tantas veces como variables haya
    print(animal)
    
numeros = [52,87,43,79]

for numero in numeros:
    resultado =numero *17
    print(resultado)

#recorrer dos arrays juntos

for numero, animal in zip(animales,numeros):
    print(f'recorriendo lista numeros: {numero}')
    print(f'recorriendo lista animales: {animal}')

#iterar en un rango

for num in range(5,10):#el primer parametro es donde arranca y el ultimo hasta que numero va, si no se ingresan parametros, empieza del 0
    print(num)

#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])

#forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#usando el else
for numero in numeros:
    print(f'valor actual: {numero}')
else:
    print('el bucle termino')

#todo lo anterior funciona igual para tuplas
