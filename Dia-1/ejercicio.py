"""
En este desafío encontrarás una función llamada solution que recibe un parámetro llamado valor. Debes encontrar el tipo de dato del parámetro valor y retornarlo desde la función solution.

Recuerda que el parámetro valor será distinto por cada distinta forma en que ejecutemos la función solution.

Ejemplo 1:

Input:
solution(1)
solution("Dieguillo")
solution(True)

Output:
"number"
"string"
"boolean"
"""

def solution(valor):
    return type(valor)

primer_valor = solution(1)
segundo_valor = solution("Dieguillo")
tercer_valor = solution(True)
print(primer_valor, segundo_valor, tercer_valor)