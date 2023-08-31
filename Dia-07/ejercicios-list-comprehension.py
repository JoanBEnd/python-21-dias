"""
En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre
las palabras que contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto
mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas
las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras 
que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:

Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

Output: ["hello", "platzi"]

Ejemplo 2:

Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: []
"""

def find_words_with_two_vowels(words):    
    lista_nueva = [ palabra for palabra in words  if contarvocales(palabra.lower()) == 2 ] 
    return lista_nueva

def  contarvocales(palabra):
    vocales = "aeiou"
    contar = 0
    for char in palabra:
        if char in vocales:
            contar =contar + 1
    
    return contar

find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi",
  "Apple"
])

find_words_with_two_vowels(["text", "test", "python", "example"])


#*************** USANDO FULL LIST COMPREHENSION
def encontrar_vocales(words):

    lista_nueva = [palabra for palabra in words if sum(1 for char in palabra if char in "aeiou" ) == 2]
    print(lista_nueva)

encontrar_vocales([
  "hello",
  "Python",
  "world",
  "platzi"
])


encontrar_vocales(["text", "test", "python", "example"])

#EJERCICIOS 2:
#Combinaciones de elementos: Encuentra todas las combinaciones posibles de dos elementos de dos listas diferentes.

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

lista_combinada_concatenada = [f"{numero}{letra}"  for numero in list1 for letra in list2]
lista_combinada_set = [ (numero, letra) for numero in list1 for letra in list2]
print(lista_combinada_concatenada)
print(lista_combinada_set)



#EJERCICIOS 3:
#Filtrar números primos: Genera una lista de los primeros 100 números primos utilizando una list comprehension.

lista_primos = [n for n in range(1, 100) if n % 2 == 0]
print(lista_primos)


#EJERCICIOS 4:
#Encontrar palíndromos: Encuentra todos los palíndromos de palabras en una lista.
words = ["radar", "python", "level", "programming", "deified"]

palindromo = [palabra for palabra in words if palabra == palabra[::-1]]
print(palindromo)

 


#EJERCICIOS 5:
#Operaciones matemáticas: Calcula el cuadrado de los números pares y el cubo de los números impares en una lista.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


resultado = [numero**2 if numero%2 == 0 else numero**3 for numero in numbers]
print(resultado)