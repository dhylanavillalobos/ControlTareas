import os

# Lista para almacenar las tareas
global lista
lista = list()

# Clase Tarea para almacenar los valores de nombre/materia/porcentaje
class Tarea:
    nombre= ""
    materia= ""
    porcentaje=0

# metodo para agregar las tarea ingresada a la lista
def agregar(nom, mat, porc):
    p = Tarea()

    p.nombre=nom
    p.materia=mat
    p.porcentaje=porc

    # Se inserta la tarea en la lista
    # Se utiliza el manejo de errores con el try except
    try:
        lista.append(p)
        print("Se ha agregado la Tarea "+ p.nombre + " a la lista de tareas.")
    except:
        print("Error al ingresar la tarea")

    input("Presione enter para continuar.")

# Imprime las tareas para una materia en especifico
def consultarMateria (mat):
    for p in lista:
       if p.materia== mat:
           print("Tarea: "+p.nombre+" / Porcentaje: "+p.porcentaje)
    input("Presione enter para continuar.")

# Imprime la cantidad de tareas que hay en la lista
def CantidadTareas ():
    cantTareas = len(lista)
    print("Tiene un total de " + str(cantTareas) + " tareas.")
    input("Presione enter para continuar.")

# Metodo para salir
def salir ():
    print("Salir")

#Se define el menu
def menu ():
    salir = False

    # se ejecuta el menu mientras la opción no sea salir
    while not salir:
        # Limpia la pantalla antes de mostrar el menú
        os.system('cls')
        
        # Muestra el Menú y las opciones
        print("       Menú     ")
        print("****************")
        print("1. Agregar Tarea")
        print("2. Consultar Tareas")
        print("3. Total de Tareas")
        print("4. Salir")

        #Se solicita la opción que desea
        opc=int(input("Digite una opción: "))

        # Si la opción es 1 se piden los datos de la tarea y se llama al metodo agregar
        if opc == 1:
            nom = input("Ingrese el nombre de la tarea que desea agregar: ")
            mat = input("Ingrese la materia a la cuál pertenece la tarea: ")
            porc = input("Ingrese porcentaje que vale la tarea: ")
            agregar(nom, mat, porc)

        # Si la opción es 2 se pide el nombre de la materia y se llama al metodo consultar materia
        elif opc == 2:
            mat = input("Ingrese el nombre de la materia que desea consultar: ")
            consultarMateria(mat)
        
        # Si la opción es 3, se muestra la cantidad de tareas que hay en la lista
        elif opc == 3:
            CantidadTareas()

        # Y finalmente 4 si se desea salir para finalizar el ciclo y cerrar el menú
        else:
            print("Salir")
            salir= True

# Se corre el menu
menu()
