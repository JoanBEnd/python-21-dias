

nuevalista = [
    {
        'id': 1,
        'name': 'Comprar leche',
        'priority': 1,
        'tags': ['shopping', 'home']
    },
    {
        'id': 2,
        'name': 'Llamar a Juan',
        'priority': 3,
        'completed': True,
        'tags': ['personal']
    }
]

# Filtrar el id de los elementos con el nombre "Llamar a Juan"
filtered_ids = [item['id'] for item in nuevalista if item['name'] == 'Llamar a Juan']

print(filtered_ids)