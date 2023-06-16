diccionario = {
    "nombre": 'lucas',
    'apellido':'dalto',
    'subs':1000000
    
}

#iterar el elemento y devolver sus valores, devuelve tupla con clave valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')