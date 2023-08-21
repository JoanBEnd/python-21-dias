#Diccionario
#Son una estructura de datos que permite almacenar una coleccion de clave-valor.
#las claves son string y se utilizan para poder acceder a los valores.

# mi_diccionario ={
#     "clave1": valor1,
#     "clave2": valor2,
#     "clave3": valor3
# }


#ejemplo:

curso = {

    "nombre": "Curso de Python",
    "duración": "20 horas",
    "clases": 100,
    "detalles":{
        "tecnologias": ["Python", "Flask","Django"],
        "calificación": 5,
    },
    "comentarios": ["Python es grandioso!!"]
}

#para acceder a los valores, usamos la notacion de corchetes y dentro de ellos especificamos la clave

print(curso["nombre"]) #Curso de Python

#Tambien, los diccionaros pueden tener metodos,los cuales son funciones asociadas a un diccionario

coche = {
    "marca": "Toyota",
    "encender": lambda: print("El carro ha sido encendido!")
}

coche["encender"]()
 