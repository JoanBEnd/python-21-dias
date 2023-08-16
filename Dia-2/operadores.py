#OPERADORES:
#Los operadores son elementos que nos permien hacer calculos y comparaciones en Python.
#A continuacion tenemos los operadores más comunes:

#OPERADORES ARITMETICOS:
#Estos operadores nos permiten hacer operaciones matematicas básicas
#A continuación un ejemplo:

#suma:
print(1 + 2) #3

#resta:
print(35-15) #20

#multiplicacion:
print(12*45) #540

#división:
print(15/3) #5

#division entera
print(14//4) #3

#módulo (devuelve el residuo de una división)
print(6 % 2) #0

#potencia
print(2**3) #8


# *****************************************************************************************

#OPERADORES DE ASIGNACIÓN:
#estos operadores permiten asignar valores a las variables

x, y, z, m, n, o, p = 10, 10, 10, 10, 10, 10, 10


x += 5
print(x)

y -= 3
print(y)

z *= 4
print(z)

m /= 2
print(m)


n //= 3
print(n)

o %= 2
print(o)

p**=3
print(p)


#OPERADORES DE COMPARACION:
#estos operadores permiten comparar valores y devuelven un True or False

print(10 > 2) #True
print(3533 < 784) #False
print(1 == 1) #True
print(2 <= 1) #False
print( 34>= 33) #True

print(2 == "2") #False
print( 3 is "3") #False
print( 4 is 4) #True


#OPERADORES LÓGICOS:
#Estos tambien nos sirven para realizar operacion de comparación y evaluación

## AND: evalua si ambas expresiones que se tenga en una condicional sean verdaderas :
mi_edad = 35
mi_signo = "Capricornio"

if mi_edad == 35 and mi_signo == "Capricornio":
    print("los datos que estás comparando son verdaderos")
else:
    print("los datos que están comparando no coinciden.")


## OR: evalua si al menos una de las expresiones es verdadera

mi_mascota ="perro"
nombre_mascota = "duke"

if mi_mascota == "perro" or nombre_mascota=="kratos":
    print("Si tiene una mascota")
else:
    print("No tienes un perro o no se llama Duke")


## NOT: este operador invierte el valor de la expresion. Si la expresion es verdadera con el not la convertiremos
# en False y si la expresion llega a ser False entonces con el NOT se convierte en True

fin_de_semana = False

if not fin_de_semana:
    print("no se trabaja")
else:
    print("Trabajamos de 8:00 am - 6:00 pm")