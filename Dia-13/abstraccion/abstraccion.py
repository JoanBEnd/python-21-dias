#La abstracción permite representar objetos y sus caracteristica de manera simplificada
#ocultnado los detalles internos de su implementacion
#La abstracción se logra usando clases, metodos y herencia

#Por ejemplo
#Tenemos un juguete con el cual estamos jugando en este caso un carro.
#Podemos presionarun boton para hacer que el auto se encienda,
#otro boton para que se apague, otro boton para acelerar y otro para frenar
#la abstraccion te permite ocultar los detalles internos que son complejos, es decir
#lo que hace cada boton, brindandote una forma facil de interactuar con el juguete
#en este caso para con el carro utilizando unos botones de un control remoto.

#detallamos en código

class Carro: #clase
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0
    
    #metodos
    def encender(self):
        self.encendido = True
        print("El carro está encendido")
    
    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print("El carro está apagado")
    
    def acelerar(self, incrementar):
        if self.encendido:            
            self.velocidad += incrementar
            print(f"El carro está acelerando a {self.velocidad} km/h")
        else:
            print(f"El carro está apagado.")
            
    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad >= decremento:
                self.velocidad -= decremento
                print(f"El carro está deshacelerando a {self.velocidad} km/h")
            else:
                self.velocidad = 0
                print("El carro a frenado por completo.")
        else:
            print("El carro está apagado.")

mi_carro = Carro("Volvo", "xc90", "negro")
print(mi_carro.marca)

mi_carro.encender()
mi_carro.acelerar(40)
mi_carro.acelerar(18)
mi_carro.apagar()
mi_carro.frenar(21)
mi_carro.frenar(21)
mi_carro.frenar(16)
mi_carro.frenar(12)

#En el ejemplo podemos ver que la clase Carro, los metodos conforman parte de la herencia
#permitiendo que la interacción para el usuario sea sencilla sin complicaciones.
#En este caso no se usó herencia pero esto también formaria parte de la abstracción