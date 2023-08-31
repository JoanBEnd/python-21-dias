"""
En este desafío implementarás una función que filtre los mensajes de un usuario específico.
La función filter_user_messages recibirá dos parámetros:

messages: una lista de mensajes
user: un nombre de usuario.
Debe devolver una nueva lista que contenga solo los mensajes del usuario especificado.

La lista messages contiene diccionarios con información sobre cada mensaje, incluyendo el remitente ('sender') y 
el contenido del mensaje ('content').

En caso de no encontrar mensajes del usuario deberá retornar una lista vacía []

Ejemplo 1:

Input:

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
filter_user_messages(messages, user)

Output:

[
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

def filter_user_messages(messages, user):
  # Tu código aquí 👈
  pass
  
"""


messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
def filter_user_messages(messages, user):
    return list(filter(lambda usuario:  usuario if usuario["sender"] == user else [] , messages))


lista_filtrada = filter_user_messages(messages, user)
print(lista_filtrada)



#Ejercicios Nivel Intermedio:

#Ordenar lista de tuplas: Dada una lista de tuplas, ordena la lista según el segundo elemento de cada tupla.

#Input: [(3, 15), (1, 10), (2, 5)]

#Output: [(2, 5), (1, 10), (3, 15)]

lista_tupla = [(3, 15), (1, 10), (2, 5)]


lista_tupla_ordenada = sorted(lista_tupla, key= lambda x: x[1])
print(lista_tupla_ordenada)

#Ejercicio
#Filtrar números primos: Dada una lista de números, filtra los números primos 
# utilizando una función lambda.

#Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Output: [2, 3, 5, 7]

#esto funciona para listas cortas
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros_primos = list(filter(lambda numeros:   sum(1 for elemento in range(1,numeros+1) if numeros % elemento == 0) == 2  , lista_numeros))
print(lista_numeros_primos)




#Si en caso se quisiera tener una lista larga se deberia usar la Criba de Eratóstenes:
#En ella primero manejamos una funcion donde se pasa como unico parametro un numero, puede ser 100 y con eso verifica los 100 primeros numeros

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False 
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

numero = 100
lista_primos = sieve_of_eratosthenes(numero)
print(lista_primos)


## Ó puede ser una lista y lo que hariamos es tomar el numero maximo de la lista y en base a ello usar la funcion la Criba de Eratóstenes
## con eso obtenemos los numeros primos y luego los comparamos con la lista que tenemos y
##para obtener los numeros primos


lista_numeros_larga = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,13, 15, 40, 55, 70, 71, 111, 115, 175, 189, 210, 213, 229, 250]


numero =max(lista_numeros_larga)
lista_primos = sieve_of_eratosthenes(numero)
lista_primos_comparando =  [elemento for elemento  in lista_primos  if elemento in lista_numeros_larga]
print(lista_primos_comparando)



#Ejercicio:
#Multiplicar elementos de una lista: Dada una lista de números, multiplica cada elemento por 2 utilizando una función lambda.

#Input: [1, 2, 3, 4, 5]
#Output: [2, 4, 6, 8, 10]

lista_numeros = [1, 2, 3, 4, 5]
numeros_duplicar = list(map(lambda x: x*2  , lista_numeros))
print(numeros_duplicar)



#Ejercicio: 
#Operaciones en listas de listas: Dada una lista de listas, realiza una operación específica en cada lista interior utilizando una función lambda.

#Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

lista_de_lista= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = list(map(lambda lista: [elemento *2 for elemento in lista] , lista_de_lista))
print(resultado)

#Ejercicio: 
#Ordenar por múltiples criterios: Dada una lista de diccionarios, ordena la lista primero 
# por el valor 'age' y luego por el valor 'name' de cada diccionario.

#Input: [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Eve', 'age': 25} ]
#Output: [ {'name': 'Eve', 'age': 25}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30} ]

datos_personales = [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Eve', 'age': 25} ] 

ordenando_datos = sorted(datos_personales, key=lambda x: (x["age"], x["name"]))
print(ordenando_datos)


data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Eve', 'age': 25}
]

sorted_data = sorted(data, key=lambda x: (x['age'], x['name']))
print(sorted_data)


#Ejercicio: 
#Conteo de palabras en lista: Dada una lista de cadenas, cuenta cuántas veces aparece 
#cada palabra en todas las cadenas utilizando una función lambda.

#Input: ['hello world', 'world of programming', 'hello programming']
#Output: {'hello': 2, 'world': 2, 'of': 1, 'programming': 3}
from collections import Counter
lista_string =  ['hello world', 'world of programming', 'hello programming']
frase = ' '.join(lista_string)
lista = {letra: sum(1 for letter in frase.split() if letter == letra ) for letra in frase.split()}

lista_counter = dict(Counter(word for phrase in lista_string for word in phrase.split()))
print((lista_counter))





 