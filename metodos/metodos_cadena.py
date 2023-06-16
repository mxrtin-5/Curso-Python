cadena1 = "hola soy gay"
cadena2 = "bienvenido"

resultado = cadena1.upper() #convierte todo en mayusc
resultado2 = cadena1.lower()#convierte todo en minuscula
resultado3 = cadena1.capitalize()#convierte la primera letra en mayuscula
resultado4 = cadena1.find("hola")#se accede a una variable y busca el valor ingresado en la respectriva variable, devuelve la posicion en la que encuentra lo que le pedimos por ej la a de hola seria el lugar 3 empezando de 0, si no hay coincidencias devuelve -1
resultado5 = cadena1.index("hola")#igual que el find pero si no hay coincidencia lanza una excepcion
resultado6 = cadena1.isnumeric()#false, pregunta si el valor ingresado es numerico
resultado7 = cadena1.isalpha()#false, pregunta si el valor ingresado es alfanumerico, los espacios no cuentan como caracteres alfanumericos
resultado8 = cadena1.count("a")#busca una cadena en otra cadena, devuelve el numero de veces que coincida
resultado9 = len(cadena1)#Devuelve la cantidad de caracteres que tiene la cadena
resultado0 = cadena1.startswith('h')#true, se envia el caracter por el que se pregunta si empieza
resultado10 = cadena1.endswith("p")#false, lo mismo que el enterior pero verifica la letra con la que termina
resultado11 = cadena1.replace("Hola capo")#reemplaza unn pedazo de la cadena dada por otra
resultado12 = cadena1.split(',')#separa la cadena por el  ,parametro ingreasdo, crea una lista




print(resultado3)