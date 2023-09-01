#La herencia en python nos permite crear nuevas clases a partir
#de clases ya existentes, heredando todas sus propiedades y metodos
#Esto permite reutilizar codigo existente

#Ejemplo

# Definimos una clase base llamada 'Animal'.
class Animal:
    # Constructor de la clase Animal.
    def __init__(self, especie):
        # Inicializamos la propiedad 'especie'.
        self.especie = especie

    # Método para hacer un sonido genérico.
    def hacerSonido(self):
        print("Este animal hace un sonido")

# Creamos una clase derivada 'Perro' que hereda de 'Animal'.
class Perro(Animal):
    # Constructor de la clase Perro.
    def __init__(self, especie, raza):
        # Llamamos al constructor de la clase base 'Animal' usando 'super()'.
        super().__init__(especie)
        # Inicializamos la propiedad adicional 'raza'.
        self.raza = raza
    
    # Método específico de la clase Perro para ladrar.
    def ladrar(self):
        print("El perro está ladrando")
  
# Explicación:
# 1. Definimos la clase base 'Animal' con una propiedad 'especie' y un método 'hacerSonido'.
# 2. Creamos la clase derivada 'Perro' que hereda de 'Animal'.
# 3. En el constructor de 'Perro', llamamos al constructor de 'Animal' usando 'super()'
#    para inicializar la propiedad 'especie' que se hereda. Luego añadimos la propiedad 'raza'.
# 4. Agregamos el método 'ladrar' específico para la clase 'Perro'.

miPerro = Perro('Canino','coker')
print(miPerro.especie)
miPerro.hacerSonido()
miPerro.ladrar()
