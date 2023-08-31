#POO es un paradigma de programacion que utiliza
#objetos y que representa cosas o conceptos del mundo real

#1: Clases.- Una claseesuna plantilla o modelo que define las propiedades de un objeto
    # Ejemplo: class MiClase:

#   Objeto.- Es una instancia de una clase, es decir se crea a partir de la clase
    # Ejemplo: objeto = MiClase()

#2: Atributos.- Los atributosson variables que se asocian a los objetos y alamacena
    #información específica de cada instancia de la clase
    #Ejemplo:   class MiClase:
    #               variable_de_clase ="Compartida"
    #           objeto = MiClase()
    #           print(objeto.variable_de_clase)

#3: Métodos.- Los metodos son funciones construidas dentro de una clase
#               y se utilizan para realizar operaciones relacionadas 
#                con los objetos de la clase


#4: Constructor.- El constructor esun étodo especial que se ejecuta automaticamente al crear
#                   el objeto. El metodo a utilizar es el __init__(), el cual se utiliza
#                 para inicializar los atributos de la clase.

# Acontinuación un ejemplo usando las 4 primeros sintaxis:
from rich import print
#clase
class Celular:
    #constructor
    def __init__(self, marca, modelo, camara):
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #metodos
    def llamar(self):
        return f"Estás realizando una llamada desde un {self.marca}"
    

primer_celular = Celular("Samsumg", "S23", "48MP")
segundo_celular = Celular("Apple", "Iphone 14", "24MP")
print("=======clase Celular==========")
print(primer_celular.marca)
print(segundo_celular.marca)

mensaje = primer_celular.llamar()
print(mensaje)


#5: Herencia.- nos permite crar nuevas clases basadas en clase ya existentes
#              La clase original se le conoce como clase base o superclase
#              y la nueva clase se llama clase derivada o subclase
#             son las subclases las que heredan los atributos y/o metodos de las suplerclases
#             en las subclase también se pueden agregar nuevos atributos que tengan relacion con la subclase


#subclase
class Persona(Celular): #Celular es la superclase
    def __init__(self, marca, modelo, camara, nombre, apellido, celular):        
        super().__init__(marca, modelo, camara)
        self.nombre =nombre
        self.apellido = apellido
        self.celular = celular
    

primera_persona = Persona("Samsumg", "A33", "36MP", "Joan", "Paredes", 945516362)
print("=========Clase Personas==========")

#accediendo a los atributos de la  suplerclase Celular
print(primera_persona.marca)
#accediendo al metodo de la suplerclase Celular
print(primera_persona.llamar())


#6: Polimorfismo.- Es la capacidad de que objetos de diferentes clases respondan
#                   a un mismo mensaje de diferentes formas, asi que el polimorfismo
#                    en python se logra a traves de implementar metodos con el mismo nombre
#                   en diferentes clases

print("==========polimorfismo==============")
class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")


def hacer_sonido(animal):
    animal.sonido()

perro = Perro()
gato = Gato()
hacer_sonido(perro)
hacer_sonido(gato)


