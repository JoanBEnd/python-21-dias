#Listas:
#las listas son una coleccion de datos que permite almacenar cualquiert tipo de valores, ya sean numeros, cadenas
#objetos, incluso otras listas

#La sintaxis de una lista en Python es la siguiente:
#   my_lista = [valor1, valor2, valor3]


#Ejemplos:

colores = ["rojo", "azul","verde"]
print(colores) #lista de colores


variados = ["Hola mundo", 35, [1, 2, 3]]
print(variados)

#Ahora la lista tiene un indice numerico y este empieza en 0. Con los ínidices podemos acceder a la ubicación
#del elemento que queremos obtener de la lista

#En el ejemplo de colores si yo quiero obtener el color azul de la lista
colores = ["rojo", "azul","verde"]

#selecciono la lista colores y comienzo a contar, la posición 0 pertene al rojo, posición 1 es el azul, entonces
#como ya tengo la posición que es el índice lo obtenemos de la siguiente manera:
print(colores[1])

#para actualizar un valor que ya se encuentra en la lista por otro valor nuevo hacemos el paso que hemos realizado
#en el caso anterior


numeros = [1, 2, 3, 4, 5]

#En la lista numeros queremos actualizar y en vez del 2 queremos cambiarlo por 8, lo que tenemos que hacer
#es identificar el indice donde se encuentra el 2 y luego reemplazarlo por el valor nuevo.

numeros[1] = 8

#entonces numeros[1] con esta sintaxis obtenemos el numero 2 ya que está en el indice 1 de la lista
# y para poder actualizarlo por el 8, le asignamos ese valor para que pueda ser reemplazado
#si volvemos a consultar la lista numeros, veremos que ha sido reemplazado el numero 2 por el 8
print(numeros)



#LOS METODOS MAS USADOS EN LAS LISTAS

#append(): Nos permite agregar un nuevo elemento al final de la lista

coloreando = ["rojo","verde", "azul"]
coloreando.append("negro")
print(coloreando)


#pop(): elimina el ultimo elemento de la lista

cartas = ["J","Q", "K", "A"]
cartas.pop()
print(cartas)

#count(): Cuenta cuantas veces un elemento está en la lista


numerando = [1,2,3,4,5,4,3,5,6,4]
print(numerando.count(4))


#extend(): Permite extender una lista agregandole los elementos de otra lista
mi_lista = [1,2,3,4]
tu_lista = [6,7,8,9]

mi_lista.extend(tu_lista)

print(mi_lista)


#reverse(): Revierte el orden de los elementos de la lista.

total_numeros = [1, 2, 3,  4, 5]
total_numeros.reverse()
print(total_numeros)


#sort(): Ordena la lista de manera ascendente o descendente.

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
print(numeros)


numeros.sort(reverse=True)
print(numeros) # [9, 6, 5, 5, 4, 3, 2, 1, 1]