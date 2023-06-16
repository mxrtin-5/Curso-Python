nombre = lambda x : x*2
#lambda es una manera de crear una funcion anonima
#lambda es una palabra clave
#retornan automaticamente
#no son aptas cuando se tiene que dar una expresion

#funcion filter
numeros = [1,2,3,4,5,6,7,8,9,13,51,346,32,12]
#se crea una funcion que indica si un numero es par o no
def es_par(num):
    if(num%2 == 0):
        return True
#usando filter con una funcion comun
numeros_pares = filter(es_par,numeros) #los parametros del filter son la funcion y el array
print(list(numeros_pares))# se hace lista para que devuelva una lista de numeros pares

#crear lo mismo con lambda

numeros_pares1 = filter(lambda numero : numero%2 == 0, numeros) #se crea una funcion anonima que tiene como parametro "numero", "numero" lo vamos a dividir por 2 y si es == 0 lo retornamos si no no retorna. La funcion filter ejecuta cada valor de un iterable, si retorna true se agrega a la lista, si no lo saca
print(list(numeros_pares1))
