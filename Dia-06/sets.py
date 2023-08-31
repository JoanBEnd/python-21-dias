#Sets:
#los set son estucturas de datos que permiten almacenar valores unicos.
#En python los set no permiten duplicados,haciendolos ideales para cuando
#se necesita una coleccion de elementos unicos.

#Sintaxis:
# my_set = set()

#Tambien se puede crear un set partiendo de una lista ya existente:

mi_lista = [1, 2, 3, 4, 5]
mi_set_lista = set(mi_lista)
print(mi_set_lista)


#Si lo declaramos de manera manual:
data = {1, 2, 3, 4, 5}
print(data, type(data))


#los sets tienen algunos metodos, a continuacion los más utilizados:

# add(value): este método agrega un valor único al set. 
#             Si se intenta agregar un valor que ya existe en el set,
#             no ocurrirá ningún cambio.
# remove(value): este método elimina un valor específico del set. Si el valor no existe, 
#                se generará un error.
# discard(value): este método elimina un valor específico del set. Si el valor no existe,
#                 no se genera ningún error.
# pop(): este método elimina y devuelve un elemento aleatorio del set.
# clear(): este método vacía completamente el set.
# len(): esta función devuelve la cantidad de elementos que existen en el set.


#ejemplos
print("*********Ejemplo con metodos*****************")
numeros_set = set()
#agregar set
numeros_set.add(1)
numeros_set.add(2)
numeros_set.add(3)

print("set completo: " , numeros_set)

print(2 in numeros_set) #True


print("mostrar longitud del set " , len(numeros_set))


numeros_set.remove(2)

print("mostrar el set despues de eliminar el 2: " , numeros_set)

numeros_set.clear()


print("mostrar el set despues de vaciar el set: " , numeros_set)

print("mostrar longitud del set " , len(numeros_set))



#Iterar set


nuevos_numeros = {6,7,8,9,10,12}

for item in nuevos_numeros:
    print(item)


#Usando slice syntax
#para usar el slice syntax ([1:])  debemos convertir el set a una lista 


my_set = {1, 2, 3, 4, 5}
my_set = list(my_set)
for item in my_set[1:]:
    print(item)


#Intersecciones: son una operación conmunente utilizadas para encontrar elementos
#que están presentes en 2 o mas sets al mismo tiempo

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}    


interseccion = set1.intersection(set2)
print("interseccion ", interseccion)