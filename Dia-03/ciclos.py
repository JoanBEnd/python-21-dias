#Ciclos:
#los ciclos son herramientas escenciales dentro de python y sirven para repetir
#un cierto bloque de codigo varias veces.
#Estos son fundamentales para la automatizacion de tareas y en la eficiencia delcódigo

#los tipos de ciclos son los "for" y los "while"


#CICLO FOR:
#Se utiliza para repetir un bloque de codigo un número especifico de veces:

#sintaxis:

#   for variable in secuencia:
#       se ejecuta el código dentro del for

#la variable es la que se estable para recorrer los elementos en la secuencia especificada

#EJEMPLO:

#en este ejemplo recorreremos el rango establecido entre el 1 y el 11, donde i sera cada 
#numero del rango exceptuando el 11 ya que es el unico valor que no se toma en el recorrido

#el resultado acá es que imprimira los numeros, 1,2,3,4,5,6,7,8,9,10
for i in range(1, 11):
    print(i)


#tambien podemos recorrer una lista, un diccionario:


#*****************recorrer una lista
lista = ["Gato", "Perro", "Tortuga", "Pescado", "Hamster"]

for elemento in lista:
    print(elemento)

#*********************recorrer diccionario

diccionario = {
    "nombre": "joan",
    "edad": 34,
    "sexo": "masculino",
    "estado": "soltero"
}

#primera forma
for llave in diccionario:
    print(llave) #aca se obtiene la llave
    print(diccionario[llave]) #aca obtenemos el valor

#segunda forma
for (llave, valor) in diccionario.items():
    print(f"la llave es: {llave} y el valor es: {valor}")



#CICLO WHILE:
#Se utiliza para repetir un bloque de codigo mientras se cumpla una condición

#sintaxis:

#   while condición:
#       se ejecuta código aquí

#lo que está haciendo es evaluar la condición y si esta es verdadera True, entonces
#ingresa al while para ejecutar el código que tiene dentro.

#EJEMPLO:

#En el siguiente ejemplo se ejecutar el while mientras la variable i sea siempre < que 10
#cuando esta variable i llegue a ser 10 entonces ya no entrara al while y el programa
#se dentendrá:

#Cada vez que la condición del while sea verdadera, dentro del while la variable i
#se le está aumentando en 1, porque si no se le aumenta seria un while infinito
# y este nunca terminará de ejecutarse.

i = 1
while i < 10:
    print(i)
    i += 1


