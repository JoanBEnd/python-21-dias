#En este desafío, deberás implementar una función personalizada que emule el comportamiento del 
#método map utilizando funciones de orden superior.

#La función recibirá dos parámetros: una lista y una función (func). La lista contendrá un conjunto
#de elementos (números, objetos, cadenas, etc.), y la función se utilizará para realizar una acción
#específica en cada elemento de la lista. El objetivo es retornar una nueva lista con los resultados 
#obtenidos de aplicar la función a cada elemento, de manera similar a como lo haría el método map.

#Ejemplo 1:

#Input: my_map([1, 2, 3, 4], lambda num: num * 2)
#Output: [2, 4, 6, 8]

#Input: my_map([
#{"name": "michi", "age": 2},
#{"name": "firulais", "age": 6}],
#lambda pet: pet["name"])

#Output: ["michi", "firulais"]

 


def my_map(list, func):
    return [func(element) for element in list]

lista = [1, 2, 3, 4]
mi_lista = my_map(lista, lambda num: num*2 )
print(mi_lista)

lista = [
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}]

mi_lista = my_map(lista, lambda pet: pet["name"] )
print(mi_lista)




#Ejercicio 1: Uso de map
#Dada una lista de números, utiliza la función map
#para elevar cada número al cuadrado y obtener una nueva lista con los resultados.

input_lista_map = [2,4,3,6,5,9,12,24,654]
output_lista_map = list(map(lambda resultado: resultado**2 ,input_lista_map))
print(output_lista_map)


#Ejercicio 2: Uso de filter
#Dada una lista de números, utiliza la función filter 
#para obtener una lista que contenga solo los números pares.

input_lista_filter =[2,4,7,1,6,8,10,22,44,32,33,11]
output_lista_filter = list(filter( lambda resultado:  resultado % 2 == 0, input_lista_filter))
print(output_lista_filter)


#Ejercicio 3: Uso de reduce
#Dada una lista de números, utiliza la función 
#reduce (importada de functools) para calcular la suma de todos los números en la lista.

from functools import reduce
input_lista_reduce = [10,20,30,40,50]
output_lista_reduce = reduce(lambda numero, sumatoria: sumatoria + numero  , input_lista_reduce)
print(output_lista_reduce)


#Ejercicio 4: Funciones lambda en map y filter
#Dada una lista de nombres en minúsculas, utiliza la función map y 
#una función lambda para convertir cada nombre a mayúsculas.

input_lista_texto = ["bienvenido", "al", "curso", "python"]
output_lista_texto = list(map(lambda texto: texto.upper(), input_lista_texto))
print(output_lista_texto)

#Dada una lista de números, utiliza la función filter y una
#función lambda para obtener una lista que contenga solo los números mayores a 50.

input_lista_filtrar_mayores = [50, 55, 32, 54, 143, 90, 84, 65, 15]
output_lista_filtrar_mayores = list(filter(lambda numeros: numeros>50, input_lista_filtrar_mayores))
print(output_lista_filtrar_mayores)


#Ejercicio 5: Uso combinado de map y filter
#Dada una lista de números, utiliza map para elevar cada número al cuadrado y 
#luego utiliza filter para obtener una lista que contenga solo los números 
#pares resultantes.


input_map_filter = [10, 45, 35, 48, 26, 87, 13]
output_map_filter = list(filter(lambda nuevo_numero: nuevo_numero %2 ==0 ,map(lambda numero: numero**2, input_map_filter)))
print(output_map_filter)










