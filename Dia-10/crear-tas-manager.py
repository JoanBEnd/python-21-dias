
"""
En este desafío, implementarás la lógica de un planificador de tareas en Python.
El objetivo es construir la función closure llamada createTaskPlanner, que devolverá
una serie de métodos para administrar las tareas. A continuación, se detallan los métodos 
que deben implementarse:

addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al 
               array de tareas. El diccionario debe contener las siguientes claves: 'id', 
               'name', 'priority', 'tags' y 'completed'. La clave 'completed' se establecerá 
               automáticamente como False al agregar una tarea.

removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.
getTasks(): devuelve el array de tareas
getPendingTasks(): devuelve solo las tareas pendientes.
getCompletedTasks(): devuelve solo las tareas completadas.

markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad 
                            (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar la
                             lista original de tareas.

filterTasksByTag(tag): filtra las tareas por una etiqueta específica. 

updateTask(taskId, updates):  busca la tarea correspondiente al id especificado y actualiza sus 
                       propiedades con las especificadas en el diccionario de actualizaciones.

Ejemplo 1:

Input: 

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')
print(planner['getCompletedTasks']())

Output:

[{
  'id': 2,
  'name': 'Llamar a Juan',
  'completed': True,
  'priority': 3,
  'tags': ['personal']
}]

"""
from rich import print

def createTaskPlanner():
    lista_tarea =[]
    def addTask(task):
        task["completed"] = False
        lista_tarea.append(task)       
    
    def removerTask(value):
        if isinstance(value, int):
            lista_tarea[:] = [lista for lista in lista_tarea  if lista["id"] != value]
        elif isinstance(value, str):
            lista_tarea[:] = [lista for lista in lista_tarea  if lista["name"] != value]
        
    
    def getTask():
        return lista_tarea
    
    def getPendingTasks():

        return [diccionario for diccionario in lista_tarea if "completed" not in diccionario or not diccionario["completed"]]

    def getCompletedTasks():
        return list(filter(lambda lista_comp:  lista_comp["completed"] == True if "completed" in lista_comp else "" ,lista_tarea))
    
    def markTaskAsCompleted(value):        
        index_lista = next((index for index, lista in enumerate(lista_tarea) if lista["name"] == value or lista["id"] == value), None)                
        lista_tarea[index_lista]["completed"] = True

    def getSortedTasksByPriority():
        return (sorted(lista_tarea, key= lambda x: x["priority"]))


    def filterTasksByTag(tag):
        return list(filter(lambda lista: lista if tag in lista["tags"] else "" , lista_tarea))
        
    def updateTask(taskId, updates):
        for tarea in lista_tarea:
            if tarea["id"] == taskId:
                tarea.update(updates)

    return {
        "addTask" : addTask,
        "getCompletedTasks" : getCompletedTasks,
        "markTaskAsCompleted": markTaskAsCompleted,
        "removerTask": removerTask,
        "getTask": getTask,
        "getPendingTasks": getPendingTasks,
        "filterTasksByTag": filterTasksByTag,
        "getSortedTasksByPriority": getSortedTasksByPriority,
        "updateTask": updateTask
    }
    

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 3,    
    'tags': ['shopping', 'home']
})

#print(planner['addTask'])


planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 1,
    'tags': ['personal']
})


planner['addTask']({
    'id': 3,
    'name': 'Comprar papas',
    'priority': 2,
    'tags': ['shopping', 'home', 'trainer']
})



(planner['markTaskAsCompleted']('Llamar a Juan'))
(planner['markTaskAsCompleted']("Comprar leche"))


#print(planner['addTask'])
letra = (planner['getCompletedTasks']())
print(f"Lista que han completado la compra",(letra))



lista_pendiente =(planner["getPendingTasks"]())
print(f"Lista pendiente de la compra",(lista_pendiente))




lista_completa = (planner['getTask']())
print(f"Lista completa",(lista_completa))

lista_filtrada = (planner["filterTasksByTag"]("trainer"))
print(f"Lista filtrada tag",(lista_filtrada))


lista_ordenada = (planner["getSortedTasksByPriority"]())
print(f"Lista ordenada",lista_ordenada)


planner["removerTask"](1)
print("Eliminando la tarea 1")
 
lista_nueva_completa = (planner['getTask']())
print(f"Lista completa nueva",(lista_nueva_completa))