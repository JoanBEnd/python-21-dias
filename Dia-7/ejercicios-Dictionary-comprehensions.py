"""
En este desafío, debes crear una función llamada count_words_by_length que recibe una lista de palabras
y devuelve un diccionario que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.

Ejemplo 1:

Input:
count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

Output:
{5: 1, 6: 2, 10: 1, 4: 2}


Input:
count_words_by_length([
  "apple",
  "banana",
  "orange"
])

Output:
{5: 1, 6: 2}
"""

# nuevo_diccionario = {clave_expresion: valor_expresion for elemento in secuencia if condicion}

def count_words_by_length(words):
    return { len(elemento): sum(1 for palabra in words if len(palabra) == len(elemento)) for elemento in words}


lista_letras  = count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

print(lista_letras)


lista_ = count_words_by_length([
  "apple",
  "banana",
  "orange"
])
print(lista_)

 


#EJERCICIOS 3:
#Contar ocurrencias de palabras: Cuenta cuántas veces aparece cada palabra en una lista de frases.

phrases = ["Hola a todos", "Hola mundo", "Hola OpenAI", "Saludos a todos"]

diccionario_frases = {texto: sum(1 for frase in phrases if texto in frase.split() )  for texto in set(' '.join(phrases).split())}
print(diccionario_frases)

 

#EJERCICIOS 4:
#Generar tablas de multiplicar: Genera un diccionario con las primeras 10 tablas de multiplicar utilizando una lista de listas.

tabla_multiplicar = { f"{numero} * {multiplicador}": numero*multiplicador  for numero in range(1, 11) for multiplicador in range(1, 11)}
print(tabla_multiplicar)


#EJERCICIOS 5:
#Conteo de letras: Dada una cadena, crea un diccionario que cuente cuántas veces aparece cada letra 
# (ignorando espacios y caracteres especiales).
#Input: "hello world"
#Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

texto = "hello world"

letras_output = { letra: sum(1 for letter in texto if letra == letter) for letra in set(' '.join(texto).split())}
print(letras_output)


#EJERCICIOS 6:
#Puntajes de estudiantes: Dada una lista de tuplas que contiene el nombre del estudiante y su puntaje,
# crea un diccionario que asigne a cada estudiante su puntaje correspondiente.

#Input: [(Alice, 85), (Bob, 92), (Eve, 78)]
#Output: {'Alice': 85, 'Bob': 92, 'Eve': 78}

estudiantes = [("Alice", 85), ("Bob", 92), ("Eve", 78)]

puntaje_estudiantes = { estudiante: nota for estudiante, nota in estudiantes }
print(puntaje_estudiantes)


#EJERCICIOS 7:
#Cuadrados de números: Dada una lista de números, crea un diccionario que asigne a cada número su cuadrado correspondiente.

#Input: [1, 2, 3, 4, 5]
#Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


numeros_al_cuadrado = [1, 2, 3, 4, 5]

elevando = { numero: numero**2 for numero in numeros_al_cuadrado}
print(elevando)


#EJERCICIOS 8:
#Longitud de palabras: Dada una lista de palabras, crea un diccionario que asigne a cada palabra su longitud.

#Input: ['apple', 'banana', 'cherry', 'date']
#Output: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

lista_palabras = ['apple', 'banana', 'cherry', 'date']
nuevas_palabras = { palabra: len(palabra) for palabra in lista_palabras }
print(nuevas_palabras)



#Conteo de palabras: Dada una cadena, crea un diccionario que cuente cuántas veces aparece cada palabra.
#Input: "the quick brown fox jumps over the lazy dog"
#Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

nueva_frase  = "the quick brown fox jumps over the lazy dog"

total_por_palabra = { palabra: sum(1 for word in nueva_frase.split(" ") if palabra == word) for palabra in set(''.join(nueva_frase).split(" ")) }
print(total_por_palabra)