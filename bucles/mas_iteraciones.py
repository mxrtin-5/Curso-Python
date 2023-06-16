frutas = ['banana','manzana','ciruela','pera','naranja','mandarina','durazno']

#evita la vuelta dependiendo de la condicion
for fruta in frutas:
    if fruta == 'mandarina':
        continue
    print(f'Me voy a a comer una {fruta}')
    
#evita que el bucle se siga ejecutando
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a a comer una {fruta}')
    
#recorrer una cadena de texto
cadena = 'hola'

for letra in cadena:
    print(letra)
    
#bucle for en luna linea

numeros = [9, 8, 34, 7]

#duplicamos los numeros
numeros_duplicados = [x*2 for x in numeros] #x es una expresion
print(numeros_duplicados)