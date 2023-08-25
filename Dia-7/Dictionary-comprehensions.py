#Dictionary comprehensions:
#Tambien es otra caracteristica poderosa Python, lo cual nos permite crear diccionarios de forma
#concisa y eficiente utiliznado una sintaxis compacta.

#sintaxis:

# nuevo_diccionario = {clave_expresion: valor_expresion for elemento in secuencia if condicion}

#clave_expresion: es una expresión que define cómo se generarán las claves del nuevo diccionario.
#valor_expresion: es una expresión que define cómo se generarán los valores del nuevo diccionario.
#elemento: es una variable que representa cada elemento de la secuencia mientras se recorre.
#secuencia: es la secuencia de origen de la cual se obtendrán los elementos.
#condicion: es una condición opcional que filtra los elementos de la secuencia.


#Ejemplos:
personas = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años

personas_mayores = { person[0]:person[1]  for person in personas if person[1] >= 25}
print(personas_mayores)

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas

longitud_personas = { nombre: len(nombre) for nombre, _ in personas }
print(longitud_personas)