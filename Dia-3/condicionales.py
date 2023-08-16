#IF:
#La estructura de contro if, sirve para tomar deciciones en función de una determinada condición
#en caso esta se cumpla (True) o no (False).
#Si la expresión o la condición se cumple, el código dentro del if se ejecutará

#A continuación se muestra la sintaxis básica:

#if condicion: <-- Cuando es verdadero ejecuta lo de adentro
    #código a ejecutar si la condicion es verdadera
#else: <-- cuando es falso  ejecuta esta linea
    #código a ejecutar si la condición no se cumple

#ejemplos:

edad = 30
if edad >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona no es mayor de edad")


#Ahora el "else", NO SIEMPRE va a ser necesario cada vez que se use la condicional if    
#Para casos que necesitemos confirmar una validación y si solo cumple con esa condicion ejecute algo adicional
#y luego la lógica continue

#ejemplo:

#Si una persona es mayor de edad, quiero que se muestre un mensaje adicional

mi_edad = 30

def mensajes_personalizado(edad):
    
    print(f"La edad de la persona es {edad} ")
    if edad >= 18:
        print("Usted por ser mayor de edad, cuenta con un descuento adicional")
    
mensajes_personalizado(mi_edad)

#Tambien se pueden manejar varias condicionales en una misma estructura:

nota = 14

if nota >= 18:
    print("Obtuvo una AD")
elif nota >= 15:
    print("Obtuvo una A")
elif nota >=11:
    print("Obtuvo una B")
elif nota >= 5:
    print("Obtuvo una C")
else:
    print("Obtuvo una D")