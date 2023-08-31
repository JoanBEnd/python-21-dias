"""
En este desafío, debes implementar la lógica de la función find_set_intersection que encuentre 
la intersección de conjuntos en una lista de conjuntos.

Recibirás un único parámetro: una lista de conjuntos. La función debe encontrar la intersección 
de todos los conjuntos de la lista y devolver el resultado como un nuevo conjunto. Si la lista está 
vacía o no hay intersección entre los conjuntos, la función debe devolver un conjunto vacío.

Ejemplo 1:
Input:
sets = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

find_set_intersection(sets)
Output: {3, 4}

Ejemplo 2:
Input:
sets = [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]
find_set_intersection(sets)
Output: set()
"""

def set_intersection(sets):
    #print(sets)
    if not sets:
        return set()
    
    first_set = sets[0]
    intersection_parcial = set()
    intersection_final = set()
    for  item_set in sets[1:]:
       intersection_parcial = first_set.intersection(item_set)
       intersection_final = intersection_parcial if len(intersection_final) == 0 else intersection_parcial.intersection(intersection_final)
    
    return intersection_final
 
    
data = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

data_final= [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]
resultado = set_intersection(data)
print(resultado)
resultado = set_intersection(data_final)
print(resultado)



print("****** usando comprehension ************")

from functools import reduce

def set_intersection_reduce(sets):
    return reduce(lambda item_first, item_second: item_first.intersection(item_second) , sets)

data = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

data_final= [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]
resultado = set_intersection_reduce(data)
print(resultado)
resultado = set_intersection_reduce(data_final)
print(resultado)