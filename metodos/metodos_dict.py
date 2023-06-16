diccionario = {
    "nombre": 'lucas',
    "apellido": 'dalto',
    "subs":1000000
}

clave1 = diccionario.keys() #devuelve las claves y tambien sirve para iterar, devuelve uin objeto dict_item

clave2 = diccionario.get("nombre")#accede al valor del elemento seleccionado (si no encuentra nada el programa continua)

diccionario.pop('nombre')#elimina el elemento indicado

diccionario_iterable = diccionario.items()#obtiene un elemento iterable