from rich import print
#Abrir archivo:
#   Para abrir un archivo de texto primero debemos abirlo en modo lectura  open()
file = open("Dia-11/archivo.txt", "r")

#Leer todo el contenido: 
#   Después para poder acceder al contenido, debemos utilizar el metod read()
content = file.read()
file.close()
print(content)

print("===================================================")
#Leer línea por línea:
#   Si deseamos leer elcontenido del archivo línea por línea
#   podemos utilizar el método readline(). Este método lee una línea a la vez
file = open("Dia-11/archivo.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

print("===================================================")

file= open("Dia-11/archivo.txt", "r")
lines = file.readlines()
lista_linea=[]
for line in lines:    
    lista_linea.append(line.replace("\n", ""))

print(lista_linea)
file.close()

#Lectura de un archivo csv

#1: Importar el modulo csv
import csv

#2: Abir el archivo csv: para ello utilizaremos la funcion open
#  y es importante especificar el modo de apertuira como "r" o "rt"

with open("Dia-11/paises.csv", "r") as file:
#3: Se crea un objeto lector CSV con la funcion reader() del modulo csv importado
#   este objeto nos permitira acceder a la información fila por fila
#   si tenemos un encabezado podemos usar DictReader()
    csv_reader = csv.DictReader(file)
#4: Leer las filas del archivo CSV. una vez que tenemos el objeto almacenado en una variable
#   este puede ser recorrido en un ciclo for para poder ver la informacion linea por linea    
    for row in csv_reader:
        print(row["Rank"], row["Country/Territory"])