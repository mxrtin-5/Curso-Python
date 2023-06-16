#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
    return numeros_sumados

resultado = suma([5,98,5678,4,789,278])
print(resultado)


#utilizando el parametro args
#operador * (args)

def suma1 (nombre, *numeros): #el asterisco define que el valor que se ingrese como parametro es una lista, convierte a todos los parametros como si fueran uno solo, se usa al final, no se pueden usar mas parametros despues de este
    return f"{nombre}, la suma de tus numeros es de: {sum(numeros)}"#agarra a los iterables y los suma
    
    
    
resultado = suma1('lucas', 678,178, 48, 423)
print(resultado)

#tambien funciona para desglosar
#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([69,423,6453,234,453])
print(resultado1)