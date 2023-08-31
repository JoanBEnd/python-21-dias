class User:  
  def __init__(self, name, age):
    #Tu código aquí 👇
    self.__name = name
    self.__age = age
    self._friends = []
    self.messages = []

  @property
  def name(self):
      return self.__name
    
  @name.setter
  def name(self, name):
    self.__name = name
    
  @property
  def age(self):
    return self.__age 
    
  @age.setter
  def age(self, age):
    self.__age = age
    
  def addFriend(self, friend):
    self._friends.append(friend)
  
  def sendMessage(self, message, friend):
    self.messages.append(message)
    friend.messages.append(message)
  
  def showMessages(self):
    return self.messages


  


usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario3 = User("Carlos", 28)
usuario1.addFriend(usuario2)
usuario1.addFriend(usuario3)
usuario1.sendMessage("Hola Maria!", usuario2)
usuario1.sendMessage("Hola Carlos!", usuario3)

print(usuario1.showMessages())
print(usuario2.showMessages())
print(usuario3.showMessages())
