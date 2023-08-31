
def calculate_discounted_price(price, discount):
    try:
        if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
            raise TypeError("El precio y el descuento deben ser números")

        if price < 0 or discount < 0:
            raise ValueError("El precio y el descuento deben ser valores positivos")
                
        return price - (price * discount)
    except ValueError as ve:
        return str(ve)
    except TypeError as te:
        return str(te)
    except Exception:
        return "Ha ocurrido un error inesperado"


primer_resultado = calculate_discounted_price(100, 0.2)
print(primer_resultado)

segundo_resultado = calculate_discounted_price(-50, 0.2)
print(segundo_resultado)

tercer_resultado = calculate_discounted_price('50', 0.2)
print(tercer_resultado)

cuarto_resultado = calculate_discounted_price(lambda x: x+ 1, 0.2)
print(cuarto_resultado)
