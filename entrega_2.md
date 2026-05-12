# Proyecto Final – Pensamiento Computacional – Docente: Juan Camilo Saldarriaga

## Equipo de Trabajo

| Nombre | Nombre |
|--------|--------|
| Mariluz Botero Gómez | María Paula Sarralde |

---

## Objetivo general

Fortalecer y evaluar las habilidades básicas del pensamiento computacional a través del desarrollo de un sistema en Python, asegurando que cada miembro del equipo pueda modificar y dar respuesta sobre el código en tiempo real durante la presentación.

## Objetivos específicos

1. Aplicar los pilares del pensamiento computacional en la resolución de problemas prácticos.
2. Implementar y dominar las estructuras de control estudiadas en clase, incluyendo: entradas y salidas de datos, condicionales simples y múltiples, ciclos while y for, manejo de listas, creación y uso de funciones, manejo de archivos y creación de gráficas.
3. Desarrollar habilidades en la creación, depuración y modificación de código, garantizando la capacidad de responder preguntas y hacer ajustes inmediatos durante la presentación del proyecto.

---

## Presentación del Proyecto

Los estudiantes deben estar en la capacidad de demostrar su comprensión y dominio del proyecto mediante actividades como:

- **Modificación de código existente:** Modificar el código del sistema actual en tiempo real durante la presentación.
- **Desarrollo de nuevas funcionalidades del sistema:** Implementar nuevas opciones, utilizando funciones y estructuras algorítmicas adecuadas, con capacidad de explicación en tiempo real.
- **Control de errores y mejoras en el sistema:** Asegurar que las acciones del sistema no generen errores lógicos, como evitar valores negativos o superar topes predefinidos. Mejorar la visualización de los datos para una mejor experiencia de usuario.
- **Fomento de la creatividad mediante la programación:** Incorporar acciones creativas y originales que añadan elementos novedosos al sistema, promoviendo la resolución de problemas de manera innovadora.

> **Nota:** Para el desarrollo de este proyecto solo puede utilizar las estructuras de programación y conceptos explicados en clase. En caso de utilizar estructuras diferentes, el estudiante debe demostrar dominio de estas y estar preparado para explicarlas.

> **Sugerencia:** Recuerde apoyarse en monitorías si tiene dudas, o preguntarle al docente.

---

## Versión FINAL del Proyecto

### Cambios realizados respecto a la Entrega 1

1. **Variables a lista:** Las 4 variables individuales (`academicos`, `hobbies`, `sociales`, `actividades`) se reemplazaron por una lista `perfil = [0, 0, 0, 0]` donde la posición 0 = Académicos, 1 = Hobbies, 2 = Sociales, 3 = Actividades.

2. **Opciones en funciones:** Cada opción del menú está implementada en una función independiente.

3. **Nuevas funcionalidades:**
   - Comparar el perfil del usuario con 5 perfiles de estudiantes predefinidos en el sistema.
   - Duplicar todos los valores usando un ciclo `for`.
   - Cambio aleatorio de una categoría.
   - Graficar el perfil con Matplotlib.

4. **Mejora de presentación:** La consulta de datos muestra la información en formato de cuadrícula.

5. **Validaciones:** Al registrar, actualizar y cargar datos, el sistema no permite valores negativos. El cambio aleatorio no permite que un valor baje de 0.

### Estructura de datos

```
perfil = [0, 0, 0, 0]
# Posición 0 = Intereses académicos
# Posición 1 = Hobbies
# Posición 2 = Afinidades sociales
# Posición 3 = Actividades universitarias
```

### Perfiles predefinidos para comparar

| Estudiante | Académicos | Hobbies | Sociales | Actividades |
|------------|-----------|---------|----------|-------------|
| Ana        | 5         | 3       | 7        | 4           |
| Carlos     | 2         | 6       | 4        | 5           |
| Lucía      | 8         | 2       | 5        | 3           |
| Mateo      | 4         | 7       | 3        | 6           |
| Sofía      | 6         | 4       | 6        | 2           |

---

## Ejemplos de interacción por cada opción del menú

### Opción 1 – Registrar valores iniciales

```
===== CAMPUSCONNECT =====
1) Registrar valores iniciales
2) Consultar valores actuales
3) Actualizar una categoría
4) Comparar afinidades
5) Guardar / cargar datos
6) Clasificar una categoría
7) Comparar con otros estudiantes
8) Duplicar todos los valores
9) Cambio aleatorio
10) Graficar perfil
11) Salir

Usuario ingresa: 1

--- REGISTRO DE DATOS ---
Cantidad de intereses académicos: 4
Cantidad de hobbies: 6
Cantidad de afinidades sociales: 3
Cantidad de actividades universitarias: 2

Sistema responde: Perfil registrado correctamente.
```

**Con valor negativo (validación):**

```
--- REGISTRO DE DATOS ---
Cantidad de intereses académicos: -1
Cantidad de hobbies: 5
Cantidad de afinidades sociales: 3
Cantidad de actividades universitarias: 2

Sistema responde: Error: No se permiten valores negativos. No se actualizaron los datos.
```

---

### Opción 2 – Consultar valores actuales

```
Usuario ingresa: 2

Sistema responde:
-------------------------
AC: 4 | HO: 6
-------------------------
SO: 3 | ACU: 2
-------------------------
```

---

### Opción 3 – Actualizar una categoría

```
Usuario ingresa: 3

Categorías:
1) Académicos
2) Hobbies
3) Sociales
4) Actividades

Usuario ingresa: 2
Ingrese el nuevo valor: 8

Sistema responde: Categoría actualizada correctamente.
```

**Con categoría incorrecta:**

```
Categorías:
1) Académicos
2) Hobbies
3) Sociales
4) Actividades

Usuario ingresa: 9

Sistema responde: Categoría incorrecta.
```

**Con valor negativo:**

```
Categorías:
1) Académicos
2) Hobbies
3) Sociales
4) Actividades

Usuario ingresa: 1
Ingrese el nuevo valor: -5

Sistema responde: Error: No se permiten valores negativos.
```

---

### Opción 4 – Comparar afinidades (máximo y mínimo)

```
Usuario ingresa: 4

Sistema responde:
Mayor afinidad: Hobbies (8)
Menor afinidad: Actividades (2)
```

> **Explicación:** El sistema recorre la lista con un ciclo `for` y compara cada valor para encontrar el mayor y el menor. Hobbies tiene 8 (el valor más alto) y Actividades tiene 2 (el más bajo).

---

### Opción 5 – Guardar / cargar datos

```
Usuario ingresa: 5

1) Guardar datos en archivo
2) Cargar datos desde archivo

Usuario ingresa: 1
Nombre del archivo (ej: perfil.txt): mi_perfil.txt

Sistema responde: Datos guardados en mi_perfil.txt
```

**Cargar datos:**

```
1) Guardar datos en archivo
2) Cargar datos desde archivo

Usuario ingresa: 2
Nombre del archivo (ej: perfil.txt): mi_perfil.txt

Sistema responde: Datos cargados desde mi_perfil.txt
```

**Cargar datos con negativos (validación):**

```
1) Guardar datos en archivo
2) Cargar datos desde archivo

Usuario ingresa: 2
Nombre del archivo (ej: perfil.txt): malos_datos.txt
(archivo contiene: -1,3,5,2)

Sistema responde: Error: El archivo contiene valores negativos. No se actualizaron los datos.
```

---

### Opción 6 – Clasificar una categoría

```
Usuario ingresa: 6

Categorías:
1) Académicos
2) Hobbies
3) Sociales
4) Actividades

Usuario ingresa: 2

Sistema responde: Hobbies: Alto nivel de intereses
```

> **Rangos de clasificación:**
> - Menos de 3 = Bajo
> - Entre 3 y 7 = Moderado
> - Más de 7 = Alto

---

### Opción 7 – Comparar con otros estudiantes

```
Usuario ingresa: 7

Sistema responde:
Tienes más afinidad con: Mateo
Diferencia total: 5
```

> **Explicación:** El sistema calcula la diferencia entre cada categoría del usuario y cada perfil predefinido. La persona con la menor diferencia total es la más afín. En este caso, el usuario tiene perfil [4, 8, 3, 2] y Mateo tiene [4, 7, 3, 6]. La diferencia total es |4-4| + |8-7| + |3-3| + |2-6| = 0+1+0+4 = 5.

---

### Opción 8 – Duplicar todos los valores

```
Usuario ingresa: 8

Sistema responde: Valores duplicados correctamente.
```

> Si los valores eran [4, 8, 3, 2], ahora son [8, 16, 6, 4].

---

### Opción 9 – Cambio aleatorio

```
Usuario ingresa: 9

Sistema responde: Se aumentó en 1: Sociales
```

> El sistema selecciona aleatoriamente una categoría y la aumenta o disminuye en 1. Si el valor ya es 0, no se puede disminuir y muestra un mensaje de error.

**Cuando el valor es 0:**

```
Sistema responde: No se puede disminuir: Actividades ya es 0.
```

---

### Opción 10 – Graficar perfil

```
Usuario ingresa: 10

Sistema responde: [Se muestra un gráfico de barras con las 4 categorías]
```

> Se muestra un gráfico de barras con las categorías en el eje X y las cantidades en el eje Y.

---

### Opción 11 – Salir

```
Usuario ingresa: 11

Sistema responde: ¡Hasta pronto!
```

---

## Código

```python
# ----------------------------------------
# PROYECTO: CampusConnect
# Versión Final - Entrega 2
# Pensamiento Computacional
# ----------------------------------------

"""
Elaborado por:
Mariluz Botero Gómez
María Paula Sarralde
Docente: Juan Camilo Saldarriaga
"""

# Librería para generar números aleatorios
import random

# Librería para graficar
import matplotlib.pyplot as plt

# ----------------------------------------
# LISTA PRINCIPAL DEL PERFIL
# Posición 0 = Intereses académicos
# Posición 1 = Hobbies
# Posición 2 = Afinidades sociales
# Posición 3 = Actividades universitarias
# ----------------------------------------
perfil = [0, 0, 0, 0]

# Nombres de las categorías para mostrar en pantalla
nombresCategorias = ["Académicos", "Hobbies", "Sociales", "Actividades"]

# Perfiles de otros estudiantes para comparar
nombresEstudiantes = ["Ana", "Carlos", "Lucía", "Mateo", "Sofía"]
perfilesEstudiantes = [
    [5, 3, 7, 4],
    [2, 6, 4, 5],
    [8, 2, 5, 3],
    [4, 7, 3, 6],
    [6, 4, 6, 2],
]


# ----------------------------------------
# FUNCIÓN 1: Registrar valores iniciales
# Permite ingresar las 4 cantidades del perfil.
# Incluye validación de valores negativos.
# ----------------------------------------
def registrarDatos():
    print(" ")
    print("--- REGISTRO DE DATOS ---")
    acad = int(input("Cantidad de intereses académicos: "))
    hobb = int(input("Cantidad de hobbies: "))
    soci = int(input("Cantidad de afinidades sociales: "))
    acti = int(input("Cantidad de actividades universitarias: "))
    if acad < 0 or hobb < 0 or soci < 0 or acti < 0:
        print("Error: No se permiten valores negativos. No se actualizaron los datos.")
    else:
        perfil[0] = acad
        perfil[1] = hobb
        perfil[2] = soci
        perfil[3] = acti
        print("Perfil registrado correctamente.")


# ----------------------------------------
# FUNCIÓN 2: Consultar valores actuales
# Muestra los datos en formato de cuadrícula.
# ----------------------------------------
def consultarDatos():
    print("-------------------------")
    print("AC: " + str(perfil[0]) + " | HO: " + str(perfil[1]))
    print("-------------------------")
    print("SO: " + str(perfil[2]) + " | ACU: " + str(perfil[3]))
    print("-------------------------")


# ----------------------------------------
# FUNCIÓN 3: Actualizar una categoría específica
# Permite modificar el valor de una sola categoría.
# Incluye validación de categoría y valor negativo.
# ----------------------------------------
def actualizarCategoria():
    print(" ")
    print("Categorías:")
    print("1) Académicos")
    print("2) Hobbies")
    print("3) Sociales")
    print("4) Actividades")
    cat = int(input("Seleccione la categoría: "))
    if cat >= 1 and cat <= 4:
        nuevo = int(input("Ingrese el nuevo valor: "))
        if nuevo < 0:
            print("Error: No se permiten valores negativos.")
        else:
            perfil[cat - 1] = nuevo
            print("Categoría actualizada correctamente.")
    else:
        print("Categoría incorrecta.")


# ----------------------------------------
# FUNCIÓN 4: Comparar afinidades
# Muestra la categoría con mayor y menor valor.
# ----------------------------------------
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


# ----------------------------------------
# FUNCIÓN 5: Guardar o cargar datos
# Sub-menú: elige si guardar o cargar.
# El usuario elige el nombre del archivo.
# Al cargar, valida que no haya valores negativos.
# ----------------------------------------
def guardarCargarDatos():
    print(" ")
    print("1) Guardar datos en archivo")
    print("2) Cargar datos desde archivo")
    accion = int(input("Seleccione una acción: "))
    if accion == 1:
        nombre = input("Nombre del archivo (ej: perfil.txt): ")
        archivo = open(nombre, "w")
        linea = str(perfil[0]) + "," + str(perfil[1]) + "," + str(perfil[2]) + "," + str(perfil[3])
        archivo.write(linea)
        archivo.close()
        print("Datos guardados en " + nombre)
    elif accion == 2:
        nombre = input("Nombre del archivo (ej: perfil.txt): ")
        if os.path.exists(nombre):
            archivo = open(nombre, "r")
            contenido = archivo.read()
            lista = contenido.split(",")
            val0 = int(lista[0])
            val1 = int(lista[1])
            val2 = int(lista[2])
            val3 = int(lista[3])
            if val0 < 0 or val1 < 0 or val2 < 0 or val3 < 0:
                print("Error: El archivo contiene valores negativos. No se actualizaron los datos.")
            else:
                perfil[0] = val0
                perfil[1] = val1
                perfil[2] = val2
                perfil[3] = val3
                print("Datos cargados desde " + nombre)
            archivo.close()
        else:
            print("Error: El archivo " + nombre + " no existe.")
    else:
        print("Acción incorrecta.")


# ----------------------------------------
# FUNCIÓN 6: Clasificar una categoría
# Clasifica según los rangos:
# Menos de 3 = Bajo
# Entre 3 y 7 = Moderado
# Más de 7 = Alto
# ----------------------------------------
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


# ----------------------------------------
# FUNCIÓN 7: Comparar con otros estudiantes
# Compara el perfil del usuario con los perfiles
# hardcodeados y muestra con quién tiene más afinidad.
# La afinidad se mide por diferencia total entre categorías.
# ----------------------------------------
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
    print("Tienes más afinidad con: " + nombreMasAfin)
    print("Diferencia total: " + str(menorDiferencia))


# ----------------------------------------
# FUNCIÓN 8: Duplicar todos los valores
# Multiplica por 2 el valor de cada categoría.
# Utiliza un ciclo for para recorrer la lista.
# ----------------------------------------
def duplicarValores():
    for i in range(len(perfil)):
        perfil[i] = perfil[i] * 2
    print("Valores duplicados correctamente.")


# ----------------------------------------
# FUNCIÓN 9: Cambio aleatorio
# Selecciona una categoría al azar y aumenta
# o disminuye su valor en 1.
# No permite que el valor baje de 0.
# ----------------------------------------
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


# ----------------------------------------
# FUNCIÓN 10: Graficar perfil
# Muestra los datos en un gráfico de barras.
# ----------------------------------------
def graficar():
    x = nombresCategorias
    y = perfil
    plt.bar(x, y, color=["#2196F3", "#4CAF50", "#FF9800", "#E91E63"])
    plt.xlabel("Categorías")
    plt.ylabel("Cantidad")
    plt.title("Perfil Campus Connect")
    plt.show()


# ----------------------------------------
# MENÚ PRINCIPAL
# ----------------------------------------
while True:
    print(" ")
    print("===== CAMPUSCONNECT =====")
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
```

---

## RÚBRICAS

### RÚBRICA TRABAJO ESCRITO (40%)

| Criterio | Excelente | Bueno | Regular | Insuficiente |
|----------|-----------|-------|---------|--------------|
| | | | | |

### RÚBRICA SUSTENTACIÓN INDIVIDUAL (60%)

> **Nota:** la sustentación de una pregunta debe ser realizada en menos de un minuto y la modificación o agregación de código en menos de dos minutos.

| Criterio | Excelente | Bueno | Regular | Insuficiente |
|----------|-----------|-------|---------|--------------|
| | | | | |

---

## Preguntas o actividades ejemplo para la sustentación
