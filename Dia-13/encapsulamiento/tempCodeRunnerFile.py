class Terceraclase:
    def __init__(self):
        self._atributo_privado = 10
    
    @property
    def atributo_publico(self):
        return self._atributo_privado
    
    @atributo_publico.setter
    def atributo_publico(self, nuevo_valor):
        self._atributo_privado = nuevo_valor


mi_clase = Terceraclase()
print(mi_clase.atributo_publico)
mi_clase.atributo_publico = 20
print(mi_clase.atributo_publico)
