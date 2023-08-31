#VARIABLES
#las variables en python se definen y se inicializan en una sola linea
#no es necesario declarar el tipo de dato

#ejemplo

numero = 30
hora = 12
mensaje = "Bienvenido"
lista = ["hola", 15, 3.5]


#FUNCIONES:
#para definir una función en python se usa la palabra reservada def
#el contenido o cuerpo de la función se escribe indentando


#ejemplo

def sumatoria(a, b):
    return a + b


#para llamar a la funcion escribimos el nombre de la funcion y pasamos los
#argumentos dentro del parentesis

sumatoria(20, 15)

#tambien podemos asignar la funcion a una variable, para que se pueda almacenar
#el resultado que devuelve la funcion
# y si queremos ver el resultado imprimimos la variable

total = sumatoria(20, 15)
print(total)



#SINTAXIS BÁSICA
#NO USA PUNTO Y COMA
#SE UTILIZA IDENTACION COMO PARTE OBLIGATORIA EN LAS FUNCIONES, CONDICIONALES, 
#LOOPS, LO CUAL ES IMPORTANTE CUANDO SE TRABAJA EN PYTHON

#PARA LOS COMENTARIOS SE UTILIZA # COMO COMENTARIO DE UNA LINEA

#PARA UN COMENTARIO MULTILINEAL ES CON """ **CONTENIDO** """
"""
MENSAJE 1
MENSAJE 2
"""


