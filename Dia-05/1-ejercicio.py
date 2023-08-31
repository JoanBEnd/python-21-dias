"""
n este desafío deberás implementar la lógica de una función que cuente
la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene
en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas 
y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:


Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}
"""
#usando logica funcional normal
def count_letters(phrase):
  # Tu código aquí 👈
  salida = {}
  for caracter in phrase:
    salida[caracter] = salida.get(caracter, 0) + 1
  
  return salida



resultado = count_letters("Hola mundo")
print(resultado)


#usando list comprehension
def count_letters_comprehension(phrase):
   
  return {caracter: phrase.count(caracter) for caracter in phrase}



resultado = count_letters("Hola mundo")
print(resultado)  