#Lista que se puede modificar 
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]

#Tupla: lista que no se puede modificar y es con ()
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

# esto modifica lo que hay en el lugar 3 del array
lista[3] = "Maquinola"

#esto no pq es inmodificable
#tupla[3] = "Maquinola"

#conjunto (set) (no se puede llamar a los elementos por su indice, no almacena datos duplicasdos)

conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto"}

#Diccionario (dict) estructura key : value (y se separa con comas)

diccionario = {
    'nombre': "Lucas Dalto",
    # key         value
    'canal': "Soy Dalto",
    'emocionado': True,
    'altura': 1.85,
    'dato_duplicado': "Soy Dalto"
}

print(diccionario['altura'])