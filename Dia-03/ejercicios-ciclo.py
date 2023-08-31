"""
En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, 
respectivamente. Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:


Input: printTriangle(3, "*")
Output:
  *
 ***
*****

Ejemplo 2:

Input: printTriangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$

"""


def print_triangle(size, character):
    espacio = size -1 
    triangle = ""
    duplicar = 1
    #en mi caso estoy recorriendo el range de mayor a menor, se agrega un valor adicional en el range, -1 que es el que permite comenzar a contar de manera descendente
    for i in range(size + 1, 1, -1):       
        
        space = " " * espacio
        caracter = character * duplicar

        #como el ultimo valor a recorrer es el 2 acá hago la condicional para no agregarle un salto de linea
        if i == 2:
           triangle +=  space  + caracter
        else:
           triangle +=  space  + caracter + "\n"

        #al hacer el recorrido de mayor a menor a los espacios les voy restando cada vez uno menos
        #y al duplicar le estoy aumentando en 2 para aumentar el caracter y si mantengan en impares
        espacio -= 1 
        duplicar += 2

    return triangle



resultado = print_triangle(3, "*")
print(resultado)

resultado = print_triangle(6, "$")
print(resultado)


resultado = print_triangle(30, "?")
print(resultado)

 