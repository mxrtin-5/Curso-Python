def frase (nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase(adjetivo = 'capo', nombre = 'lucas', apellido ='dalto')# asi se pueden forzar las posiciones de los valores de los parametros
print(frase_resultante)


#crear la funcion anterior con un parametro opcional y uno por defecto

def frase1(nombre,apellido, adjetivo = 'tonto'): #el parametro opcional es adjetivo y el valor or defecto es "tonto"
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante1 = frase('lucas', 'dalto', 'inteligente')
print(frase_resultante1)