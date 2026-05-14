#grafico a color
import matplotlib.pyplot as plt
#genera datos aleatorios
import random
#lee archivos
import os

#se usa para mostrar el grafico
import matplotlib
matplotlib.use('TkAgg')

print("Librerías importadas correctamente.")



# Variables globales y datos

# ----------------------------------------
# LISTA PRINCIPAL DEL PERFIL
# Posición 0 = Intereses académicos
# Posición 1 = Hobbies
# Posición 2 = Afinidades sociales
# Posición 3 = Actividades universitarias
# ----------------------------------------
perfil = [0, 0, 0, 0]
nombreUsuario = ""

nombresCategorias = ["Académicos", "Hobbies", "Sociales", "Actividades"]

# Perfiles de otros estudiantes para comparar
nombresEstudiantes = ["Ana", "Carlos", "Lucía", "Mateo", "Sofía"]
#matrix (listas dentro lista)
perfilesEstudiantes = [
    [5, 3, 7, 4],
    [2, 6, 4, 5],
    [8, 2, 5, 3],
    [4, 7, 3, 6],
    [6, 4, 6, 2],
]

print("Variables inicializadas. Perfil: " + str(perfil))
print("Estudiantes disponibles: " + str(nombresEstudiantes))


# Funciones del sistema

# FUNCIÓN 1: Registrar valores iniciales
def registrarDatos():
    global nombreUsuario
    print(" ")
    print("--- REGISTRO DE DATOS ---")
    nombreUsuario = input("Tu nombre: ")
    print("(Ingresa valores entre 0 y 10)")
    acad = int(input("Cantidad de intereses académicos: "))
    hobb = int(input("Cantidad de hobbies: "))
    soci = int(input("Cantidad de afinidades sociales: "))
    acti = int(input("Cantidad de actividades universitarias: "))
    if acad < 0 or hobb < 0 or soci < 0 or acti < 0:
        print("Error: No se permiten valores negativos. No se actualizaron los datos.")
    elif acad > 10 or hobb > 10 or soci > 10 or acti > 10:
        print("Error: Los valores deben estar entre 0 y 10. No se actualizaron los datos.")
    else:
        perfil[0] = acad
        perfil[1] = hobb
        perfil[2] = soci
        perfil[3] = acti
        print("Perfil registrado correctamente para " + nombreUsuario + ".")


# FUNCIÓN 2: Consultar valores actuales (cuadrícula)
def consultarDatos():
    print("-------------------------")
    if nombreUsuario != "":
        print("  Usuario: " + nombreUsuario)
        print("-------------------------")
    print("AC: " + str(perfil[0]) + " | HO: " + str(perfil[1]))
    print("-------------------------")
    print("SO: " + str(perfil[2]) + " | ACU: " + str(perfil[3]))
    print("-------------------------")


# FUNCIÓN 3: Actualizar una categoría
def actualizarCategoria():
    print(" ")
    print("Categorías:")
    print("1) Académicos")
    print("2) Hobbies")
    print("3) Sociales")
    print("4) Actividades")
    cat = int(input("Seleccione la categoría: "))
    if cat >= 1 and cat <= 4:
        print("(Valor entre 0 y 10)")
        nuevo = int(input("Ingrese el nuevo valor: "))
        if nuevo < 0 or nuevo > 10:
            print("Error: El valor debe estar entre 0 y 10.")
        else:
            perfil[cat - 1] = nuevo
            print("Categoría actualizada correctamente.")
    else:
        print("Categoría incorrecta.")


# FUNCIÓN 4: Comparar afinidades (máximo y mínimo)
def compararAfinidades():
    mayor = perfil[0]
    posMayor = 0
    menor = perfil[0]
    posMenor = 0
    for i in range(1, 4):
        if perfil[i] > mayor:
            mayor = perfil[i]
            posMayor = i
        if perfil[i] < menor:
            menor = perfil[i]
            posMenor = i
    print(" ")
    print("Mayor afinidad: " + nombresCategorias[posMayor] + " (" + str(mayor) + ")")
    print("Menor afinidad: " + nombresCategorias[posMenor] + " (" + str(menor) + ")")


# FUNCIÓN 5: Guardar o cargar datos (incluye nombre)
def guardarCargarDatos():
    global nombreUsuario
    print(" ")
    print("1) Guardar datos en archivo")
    print("2) Cargar datos desde archivo")
    accion = int(input("Seleccione una acción: "))
    if accion == 1:
        nombre = input("Nombre del archivo (ej: perfil.txt): ")
        archivo = open(nombre, "w")
        linea = nombreUsuario + "," + str(perfil[0]) + "," + str(perfil[1]) + "," + str(perfil[2]) + "," + str(perfil[3])
        archivo.write(linea)
        archivo.close()
        print("Datos guardados en " + nombre)
    elif accion == 2:
        nombre = input("Nombre del archivo (ej: perfil.txt): ")
        #busca si hay archivos guardados con este nombre
        if os.path.exists(nombre):
            archivo = open(nombre, "r")
            contenido = archivo.read()
            #separa el texto por comas en las listas
            lista = contenido.split(",")
            nombreUsuario = lista[0]
            val0 = int(lista[1])
            val1 = int(lista[2])
            val2 = int(lista[3])
            val3 = int(lista[4])
            if val0 < 0 or val1 < 0 or val2 < 0 or val3 < 0:
                print("Error: El archivo contiene valores negativos. No se actualizaron los datos.")
            else:
                perfil[0] = val0
                perfil[1] = val1
                perfil[2] = val2
                perfil[3] = val3
                print("Datos cargados desde " + nombre + " para " + nombreUsuario)
            archivo.close()
        else:
            print("Error: El archivo " + nombre + " no existe.")
    else:
        print("Acción incorrecta.")


# FUNCIÓN 6: Clasificar una categoría
def clasificarCategoria():
    print(" ")
    print("Categorías:")
    print("1) Académicos")
    print("2) Hobbies")
    print("3) Sociales")
    print("4) Actividades")
    cat = int(input("Seleccione la categoría: "))
    if cat >= 1 and cat <= 4:
        valor = perfil[cat - 1]
        nombre = nombresCategorias[cat - 1]
        if valor < 3:
            print(nombre + ": Bajo nivel de intereses")
        elif valor >= 3 and valor <= 7:
            print(nombre + ": Moderado nivel de intereses")
        else:
            print(nombre + ": Alto nivel de intereses")
    else:
        print("Categoría incorrecta.")


# FUNCIÓN 7: Comparar con otros estudiantes
def compararConPerfiles():
    menorDiferencia = 999
    nombreMasAfin = ""
    for i in range(len(perfilesEstudiantes)):
        diferencia = 0
        for j in range(4):
            diff = perfil[j] - perfilesEstudiantes[i][j]
            if diff < 0:
                diff = diff * -1
            diferencia = diferencia + diff
        if diferencia < menorDiferencia:
            menorDiferencia = diferencia
            nombreMasAfin = nombresEstudiantes[i]
    print(" ")
    if nombreUsuario != "":
        print(nombreUsuario + ", tienes más afinidad con: " + nombreMasAfin)
    else:
        print("Tienes más afinidad con: " + nombreMasAfin)
    print("Diferencia total: " + str(menorDiferencia))


# FUNCIÓN 8: Duplicar todos los valores (ciclo for)
#cada resultado se duplica , osea se aumenta 2 a un rago por ej de 4 a 6
def duplicarValores():
    for i in range(len(perfil)):
        perfil[i] = perfil[i] * 2
    print("Valores duplicados correctamente.")


# FUNCIÓN 9: Cambio aleatorio
def cambioAleatorio():
    aleatorio = random.randint(0, 3)
    operacion = random.randint(1, 2)
    if operacion == 1:
        perfil[aleatorio] = perfil[aleatorio] + 1
        print("Se aumentó en 1: " + nombresCategorias[aleatorio])
    else:
        if perfil[aleatorio] > 0:
            perfil[aleatorio] = perfil[aleatorio] - 1
            print("Se disminuyó en 1: " + nombresCategorias[aleatorio])
        else:
            print("No se puede disminuir: " + nombresCategorias[aleatorio] + " ya es 0.")


# FUNCIÓN 10: Graficar perfil
def graficar():
    x = nombresCategorias
    y = perfil
    plt.bar(x, y, color=["#2196F3", "#4CAF50", "#FF9800", "#E91E63"])
    plt.xlabel("Categorías")
    plt.ylabel("Cantidad")
    titulo = "Perfil Campus Connect"
    if nombreUsuario != "":
        titulo = "Perfil de " + nombreUsuario
    plt.title(titulo)
    plt.show()


print("10 funciones cargadas correctamente.")



# Archivo de datos de prueba
archivo = open("datos.txt", "w")
archivo.write("Paula,4,6,3,2")
archivo.close()
print("Archivo datos.txt creado con valores: Paula, 4, 6, 3, 2")
print("Ubicación: " + os.path.abspath("datos.txt"))

#Visualización de resultados
# Cargar datos de ejemplo para la visualización
nombreUsuario = "Paula"
perfil[0] = 2
perfil[1] = 6
perfil[2] = 3
perfil[3] = 2

print("Perfil de ejemplo - " + nombreUsuario + ": " + str(perfil))
print()
graficar()


#Menu Principal
while True:
    print(" ")
    print("===== CAMPUSCONNECT =====")
    if nombreUsuario != "":
        print("  Usuario: " + nombreUsuario)
    print("=========================")
    print("1) Registrar valores iniciales")
    print("2) Consultar valores actuales")
    print("3) Actualizar una categoría")
    print("4) Comparar afinidades")
    print("5) Guardar / cargar datos")
    print("6) Clasificar una categoría")
    print("7) Comparar con otros estudiantes")
    print("8) Duplicar todos los valores")
    print("9) Cambio aleatorio")
    print("10) Graficar perfil")
    print("11) Salir")
    print("(Los valores de las categorías deben estar entre 0 y 10)")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        registrarDatos()
    elif opcion == 2:
        consultarDatos()
    elif opcion == 3:
        actualizarCategoria()
    elif opcion == 4:
        compararAfinidades()
    elif opcion == 5:
        guardarCargarDatos()
    elif opcion == 6:
        clasificarCategoria()
    elif opcion == 7:
        compararConPerfiles()
    elif opcion == 8:
        duplicarValores()
    elif opcion == 9:
        cambioAleatorio()
    elif opcion == 10:
        graficar()
    elif opcion == 11:
        print("¡Hasta pronto!")
        break
    else:
        print("Opción incorrecta.")
