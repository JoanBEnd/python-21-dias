#Las High Order Functions
#son funciones que cumplen al menos uno de los siguientes criterios:

#Toman una o más funciones como argumentos
#Devuelven una función como resultado

#En Python algunas delas High ORder Functions incorporadas más comunes son:

#map(funcion, secuencia)
#filter(funcion, secuencia)
#reduce(funcion, secuencia)
#sorted(secuencia, key=función)


def operacion_matematica(fun, a, b):
    return fun(a, b)


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


resultado = operacion_matematica(suma, 15, 42)
print(resultado)