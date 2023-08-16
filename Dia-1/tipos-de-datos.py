#Numbers:
#son tipos de datos que representan tupos de datos numericos, que van desde
#enteros hasta decimales

edad = 34
pi = 3.14
sueldo = 6500.15

#***************************************************************************************

#STRINGS:
#Las cadenas de texto representan una secuencia de caracteres:
#podemos crear strings utilizando las comillas dobles "" o comillas simples ''

nombre = "Joan santiago"
pais = "Perú"

# para concatenar podemos usar el simbolo + 

mensaje = "Mi nombre es " + nombre + " y soy de " + pais
print(mensaje)

#otra forma de poder concatenar es usar la notacion f-strings de la siguiente manera:

print(f"Hola mi nombre es {nombre} y soy de {pais}")


#para los Strings, python nos proporciona unos metodos para la manipulacion:

vision = "Ser un gran Data Analitycs"

print(len(vision)) #resultado: 26
print(vision.upper()) #resultado: SER UN GRAN DATA ANALITYCS
print(vision.lower()) #resultado: ser un gran data analitycs
print(vision.split("a")) #resultado: ['Ser un gr', 'n D', 't', ' An', 'litycs']

#***************************************************************************************

#DICCIONARIOS:

#Son Estrcutura de datos, que permite almacenar un conjunto de pares clave - valor.
#Un diccionario se crea usando las {} y especificar los elementos dentro de este
# mediante la sintaxis clave : valor => {clave: valor}.
#A continuación un ejemplo

diccionario_personal = {
    "nombre": "joan",
    "apellido": "paredes",
    "edad": 33,
    "cursos": ["Fundamentos de python",
               "Comprehension",
               "POO",
               "Analisis computacional"
              ]
}
print(diccionario_personal)

#Si queremos acceder a los elementos del diccionario, podemos utilizar la clave
#que es el indice:

print(diccionario_personal["nombre"]) #joan
print(diccionario_personal["cursos"]) #['Fundamentos de python', 'Comprehension', 'POO', 'Analisis computacional']
# en este caso como uno de los elementos es una lista, para poder acceder a los elementos de
# la lista, usamos el indice de esa lista, el cual es [0].
# los indices se comienzan a contar o considerar desde la posicion 0
print(diccionario_personal["cursos"][0]) # Fundamentos de python

#**********************************************************************************

#BOOLEANOS
#Los valores booleanos son un tipo de datos que son representados por True or False

curso_completado = True
lectura_completada = False

#Estos tipos nos pueden servir para poder trabajar condicionales, en caso se cumplan
# poder ejecutar las lineas de codigo que se tengan:

#La condicional if se  explica en el Dia-3 archivo condicionales.py
if curso_completado :
    print("Vás por buen camino en tu aprendizaje!!")

if not lectura_completada :
    print("Por favor completa la lectura")



#para poder identificar el tipo de datos podemos usar type

mi_titulo ="Ingeniero"
mi_lista = [1, 2, 3, 4]
mi_edad = 34
print(type(mi_titulo))
print(type(mi_lista))
print(type(mi_edad))