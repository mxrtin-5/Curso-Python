#crear una funcion simple
def saludar():
    print('hola capo')

#se ejecuta la funcion simple
saludar()


#funcion con parametros
def saludar1(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'no lo sabemos'
    
        
    print(f'Hola {nombre}, mi {adjetivo}, como estas?')
    
saludar1('Cammila', 'mUJer')

def crear_contrasenia_random(num):
    chars = "abcdefghij" # se crean caracteres aleatorios
    num_entero = str(num)# con numero_entero, convertimos a string el numero ingresado, ya que convirtiendolo a string para que lo detecte como string y que la posicion 0 sea el primer numero ingresado
    num = int(num_entero[0])#convierte a numero entero y obtiene la posicion 0 del numero ingresado
    c1 = num - 2 #si num es por ej = 7, c1 vale 5
    c2 = num
    c3 = num - 5
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contrasenia)

password = crear_contrasenia_random(3)
frase = f"tu contrasenia nueva es: {password}"
print(frase)