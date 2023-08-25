
nueva_frase  = "the quick brown fox jumps over the lazy dog"
print(set(''.join(nueva_frase).split(" ")))
print([word for word in nueva_frase.split(" ") ])
total_por_palabra = { palabra: sum(1 for word in nueva_frase.split(" ") if palabra == word) for palabra in set(''.join(nueva_frase).split(" ")) }
print(total_por_palabra)