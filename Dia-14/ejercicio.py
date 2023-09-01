class Animal:
  def __init__(self, name, age, specie):
    self.name = name
    self.age = age
    self.specie = specie
    

  def getInfo(self):
    mi_objeto = {"name":self.name, 
                  "age": self.age, 
                  "specie": self.specie
                }
    print(mi_objeto)

class Mammal(Animal):
  def __init__(self, name, age, specie, hasFur):
    super().__init__(name, age, specie)
    self.hasFur = hasFur
    
  def getInfo(self):
    mi_objeto = {"name":self.name, 
                  "age": self.age, 
                  "specie": self.specie,
                  "hasFur": self.hasFur,
                }
    print(mi_objeto)


class Dog(Mammal):
  def __init__(self, name, age,  breed):
    super().__init__(name, age, specie="dog", hasFur = True)
    self.breed = breed    
  
  def getInfo(self):
    mi_objeto = {"name":self.name, 
                  "age": self.age, 
                  "specie": self.specie,
                  "hasFur": self.hasFur,
                  "breed" : self.breed,
                }
    print(mi_objeto)
  
  def bark(self):    
    print("woof!")

print("======primer ejemplo=========")

bird = Animal("pepe", 1, "bird")
bird.getInfo()

print("======segundo ejemplo=========")

hippo = Mammal("bartolo", 3, "hippo", False)
hippo.getInfo()



print("======tercer ejemplo=========")
dog = Dog("fido", 4, "pastor aleman")
dog.bark()
dog.getInfo()
