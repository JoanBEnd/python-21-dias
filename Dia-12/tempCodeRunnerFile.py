class Perro():
    def sonido(self):
        print("Guau")

class Gato():
    def sonido(self):
        print("Miau")


def hacer_sonido(animal):
    animal.sonido()

perro = Perro()
gato = Gato()
hacer_sonido(perro)
hacer_sonido(gato)
