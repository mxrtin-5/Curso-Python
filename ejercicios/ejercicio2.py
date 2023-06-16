#falto un profesor de clases y los alumnos que son 10 se organizaron para hacer la suya propia, uno de los alumnos va a ser el profesor y el otro el asistente
#a) pedir el nombre y esdad de los alumnos que vinieron hoy a clase y ordenarlos de menor a mayor
#b) el mayor de la clase es el profesor y el menor el asistente, quien es quien

numero_alumnos = 4
alumnos = [] #crea una lista de tuplas

for i in range(numero_alumnos):
    nombre = input(f'Ingrese el nombre del alumno numero {i+1} ')
    edad = int(input(f'Ingrese la edad del aluumno {i+1} '))
    alumnos.append((nombre,edad)) #append() se utiliza para agregar cada tupla que contiene el nombre y la edad de cada alumno a la lista alumnos

#ordenar los alumnos de menor a mayor
alumnos_ordenados = sorted(alumnos, key = lambda x:x[1])#sorted() es un método de Python que se utiliza para ordenar una lista. En este caso, se utiliza para ordenar la lista alumnos por edad, de menor a mayor.  toma dos argumentos: la lista que se desea ordenar (alumnos) y una función key opcional que especifica el criterio de ordenamiento. 

profesor = alumnos_ordenados[-1]
asistente = alumnos_ordenados [0]

print(f"El profesor es {profesor[0]} con {profesor[1]} años y el asistente es {asistente[0]} con {asistente[1]} años.")
