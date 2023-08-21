#Tuplas:
#son objetos que permiten almacenar colecicon de valores, a diferencia
#de las listas, estas son inmutables, es decir no se pueden modificar
#despues de haberse creado
#Sintaxis:
#   mi_tupla = (valor1, valor2, valor3)

puntos = ((1,2),(3,4),(5,6))

#las tuplas tambien tienen indices numericos que empiezan en 0
#asi para poder acceder al primer elemento de la tupla utilizadmos
#la sintanxis puntos[0]
print(puntos[0])
print(type(puntos[0]))


#Como se indica, las tuplas son inmutables, por lo que si queremos modificar
#un elemento dentro de la tupla, nos marca un error

puntos[0] = 2
print(puntos)


#si queremos hacer un cambio, lo que se puede hacer es crear una nueva tupla
#a partir de la ya existente
#sintaxis:
# nueva_tupla =  typla[:indice] + (nuevo_valor) + tupla[indice+1:]


mis_puntos = ((1,2),(3,4),(5,6))
nuevos_puntos = (7,8)

#mis_puntos[:1] -> esto obiene (1,2)
#mis_puntos[1:2] -> esto obiene (3,4)
#mis_puntos[2:] -> esto obiene (5,6)

mis_puntos_nuevos = mis_puntos[:1] + (nuevos_puntos,) + mis_puntos[2:]
print(mis_puntos_nuevos)


#A continuación algunos metodos para las tuplas

#index:
mis_datos  = ((1,2),(3,4),(5,6))
print(mis_datos.index((3,4))) #1 nos indica en que indice se encuentra


#count: te duevelve cuantas veces se repite un numero en la tupla
mis_numeros = (1,2,3,4,32,2,5,23,4,6,7,3)
print(mis_numeros.count((3)))

#len(): retorna la cantidad de elementos que hay en una tupla
print(len(mis_numeros))