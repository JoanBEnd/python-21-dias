def get_student_average(students):
    suma = 0
    lista_output = {
        "class_average": 0,
        "students": []
    }

    for items in students:
        suma += sum(items["grades"])/ len(items["grades"])

        lista_output["students"].append({
            "name": items["name"],
            "average": round(sum(items["grades"])/ len(items["grades"]),2)
        })

    average_class = round(suma / len(students) , 2)
    lista_output["class_average"] = average_class

    return lista_output
       

resultado = get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])
print(resultado)