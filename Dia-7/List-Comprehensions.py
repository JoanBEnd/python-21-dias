#list comprehensions:
#Es una caracteristica poderosa de Python, que nos permite crear listas de forma
#concisa y eficiente utilizando una sintaxis compacta

#Sintaxis:
# nueva_lista = [expresion for elemento in lista_original if condicion]

# expresion: es una expresión que define cómo se transformarán los elementos de la lista original
#            para obtener los elementos de la nueva lista.
# elemento: es una variable que representa cada elemento de la lista original mientras se recorre.
# lista_original: es la lista de origen de la cual se obtendrán los elementos.
# condicion: es una condición opcional que filtra los elementos de la lista original.

#Ejemplos:

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con el cuadrado de los números pares de la lista original

cuadrado_pares = [numero**2  for numero in numeros if numero % 2 == 0]
print(cuadrado_pares)

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original

impares_por_dos = [numero * 2 for numero in numeros if numero % 2 == 1]
print(impares_por_dos)


# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares

lista_numeros = [f"{numero} es par" if numero % 2 == 0  else f"{numero} es impar" for numero in numeros ]
print(lista_numeros)