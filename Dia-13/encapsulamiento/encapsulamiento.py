#Encapsulamiento se refiere ala idea de que los datos y metodos de
#un obketo deben estar protegidos yno deben ser accesibles directamente
#desde fuera del objeto
#Para esto el encapsulamiento se logra utilizando coneviones de nomenclatura,
#para el caso de propiedades mediante el decorador @property


#1 Convenciones de Nomenclatura: En python se utiliza convenciones de nomenclatura
# para indicar el nivel de accecibilidad de los atributos y metodos de una clase

#PAra un atributo o metodo privado: La convencion a utilizar es un guion bajo (_) 
#al inicio de un nombre de atributo o metodo

class MiClase:
    def __init__(self):
        self._atributo_privado = 10
    
    def _metodo_privado(self):
        pass


#2 Decorador @property: En python usamos este decorador para crear un metodo getter para
# acceder a un atributo privado como si fuera propiedad publica.

class SegundaClase:
    def __init__(self):
        self._atributo_privado = 10
    
    @property
    def atributo_publico(self):
        return self._atributo_privado

#Como se puede observar en este ejemplo, el atributo _atributo_privado es un atributo privado, pero
#se puede acceder a él desde fuera de la clase, utilizando el metodo getter atributo_publico

mi_obejto = SegundaClase()
print(mi_obejto.atributo_publico)


#Setter utilizando el decorador @nombre_de_la_propiedad.setter. En python tambien podemos
#usar este decorador para crear un metodo de tipo setter, que permita crear un atributo privado

class TerceraClase:
    def __init__(self):
        self._atributo_privado = 10
    
    @property
    def atributo_publico(self):
        return self._atributo_privado
    
    @atributo_publico.setter
    def atributo_publico(self, nuevo_valor):
        self._atributo_privado = nuevo_valor


mi_clase = TerceraClase()
print(mi_clase.atributo_publico)
mi_clase.atributo_publico = 20
print(mi_clase.atributo_publico)



#Metodos y atributos privados: Se considera una convencion que los metodos y atributos que 
#comienzan con 2 guiones bajos (__) sean tratados como privados y no sean accedidos directamtente
#desde fuera de la clase.

class MiClasePrivada:
    def __init__(self):
        self.__atributo_privado = 10
    
    def __metodo_privado(self):
        pass

#En este ejemplo, el atributo __atributo_privado y el método __metodo_privado son privados, 
#pero Python los renombra internamente utilizando el nombre de la clase que los contiene para evitar 
#conflictos con clases derivadas. Por ejemplo, el atributo __atributo_privado se renombraría a
#_MiClase__atributo_privado internamente.

