

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Article(Product):
    def addToCart(self):
        return f"Agregando {self.quantity} unidades del artículo {self.name}"

class Service(Product):
    def addToCart(self):
        return f"Agregando el servicio {self.name} al carrito"

class Cart:
    def __init__(self):
        self.products = []
  
    def addProduct(self, product):
        added_message = product.addToCart()
        self.products.append(product)
        return added_message

    def deleteProduct(self, product):
        self.products = [item for item in self.products if item.name != product.name]
  
    def calculateTotal(self):
        total = sum(item.price * item.quantity for item in self.products)
        return total
  
    def getProducts(self):
        return self.products

# Crear productos
article1 = Article("Camiseta", 20, 2)
service1 = Service("Limpieza", 50, 1)

# Crear carrito
my_cart = Cart()

# Agregar productos al carrito
added_article_message = my_cart.addProduct(article1)
added_service_message = my_cart.addProduct(service1)

# Obtener productos en el carrito
cart_products = my_cart.getProducts()

# Calcular el total
total_price = my_cart.calculateTotal()

# Imprimir resultados
print(added_article_message)
print(added_service_message)
print("Productos en el carrito:", cart_products)
print("Total:", total_price)