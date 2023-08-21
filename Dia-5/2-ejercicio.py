"""
En este desafío, debes crear una función que encuentre el palíndromo más largo 
en una lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún 
palíndromo en la lista, la función debe devolver None. Si hay más de un palíndromo
con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante 
como hacia atrás.

Ejemplo 1:


Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

Output: "racecar"

"""
 

def find_largest_palindrome(words):
    output = None

    for items in words:
        new_texto =""
        for caracter in reversed(items):
            new_texto += caracter

        if new_texto == items:
            if output == None:
                output = new_texto
            elif len(new_texto) > len(output):
                output = new_texto

    return output


find_largest_palindrome(["racecar", "level", "world", "hello"])
find_largest_palindrome(["Platzi", "Python", "django", "flask"])