#Funciones Lambda:
#Estas funciones en python son anónimas, las cuales se definen de manera concisa en una sola linea

#Sintaxis:
# lambda argumentos: expresion

#argumentos: son los parametrosde la funcion
#expresión: es la operación que se realizará y devolverá el resultado

#Las funciones lambda se utilizan en combinación con otras funciones, las cuales son
#map(), filter(), reduce()

#Ejemplos:

# Ejemplo 1: Función lambda simple

suma = lambda a,b: a + b
resultado = suma(5, 12)
print(resultado)

#Uso de lambda con map()
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x**2, numeros))
print(duplicados)


#Ejemplo 3: Uso de lambda con filter()
numeros = [1, 2, 3, 4, 5]
lista_filtrada = list(filter(lambda elemento : elemento % 2 == 0  ,numeros))
print(lista_filtrada)

