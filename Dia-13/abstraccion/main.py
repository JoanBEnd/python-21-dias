from rich import print
from product import Product

class Article(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    
    def addToCart(self):
        print(f"Agregando {self.quantity} unidades del  artículo {self.name} al carrito")



class Service(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def addToCart(self):
        print(f"Agregando el servicio {self.name} al carrito")

class Cart:
    def __init__(self):
        self.product = []

    def addProduct(self, product):
        self.product.append(product)
        product.addToCart()

    def deleteProduct(self, product):
        self.product.remove(product)

    def calculateTotal(self):        
        total = 0        
        for producto in self.product:                        
            total += producto.price * producto.quantity        
        print(total)

    def getProducts(self):
        return self.product
    



book = Article("Libro", 100, 2);
course = Service("Curso", 120, 1);

cart = Cart();
cart.addProduct(book);
cart.addProduct(course);
cart.calculateTotal();
data = cart.getProducts()
print(data)

 