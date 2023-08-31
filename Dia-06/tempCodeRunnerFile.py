
from functools import reduce

def set_intersection_reduce(sets):
    return reduce(lambda x,y: x.intersection(y) , sets)

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