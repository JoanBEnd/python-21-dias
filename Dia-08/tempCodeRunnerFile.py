
input_map_filter = [10, 45, 35, 48, 26, 87, 13]
output_map_filter = list(filter(lambda nuevo_numero: nuevo_numero %2 ==0 ,map(lambda numero: numero**2, input_map_filter)))
print(output_map_filter)