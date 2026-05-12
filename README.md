# Campus Connect - Entrega 2

Aplicación de terminal en Python para registrar y gestionar perfiles de afinidades universitarias.

## Integrantes

- Mariluz Botero Gómez
- María Paula Sarralde

**Docente:** Juan Camilo Saldarriaga

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `campus_connect.ipynb` | Notebook de Jupyter/Colab con el proyecto completo |
| `campus_connect.py` | Código Python independiente (mismo código que el notebook) |
| `datos.txt` | Archivo de datos de prueba (`4,6,3,2`) |
| `docker-compose.yml` | Entorno Jupyter en puerto 8889 |
| `entrega_2.md` | Documento de entrega con ejemplos de interacción |
| `plantilla_entrega_2.md` | Plantilla original del docente |

## Cómo ejecutar

### Opción 1: Docker (local)

```bash
docker compose up -d
```

Abrir `http://localhost:8889` y ejecutar las celdas de `campus_connect.ipynb` en orden.

### Opción 2: Google Colab

Subir `campus_connect.ipynb` a Google Colab y ejecutar las celdas en orden.

## Estructura del notebook

1. **Portada** - Título, integrantes, descripción
2. **Preparación** - Imports (`matplotlib`, `random`, `os`)
3. **Variables** - Lista `perfil = [0, 0, 0, 0]` y perfiles hardcodeados
4. **Funciones** - 10 funciones independientes
5. **Datos prueba** - Crea `datos.txt`
6. **Visualización** - Gráfica demo con datos de ejemplo
7. **Menú** - Sistema interactivo con 11 opciones

## Menú de opciones

| # | Opción | Función | Qué hace |
|---|--------|---------|----------|
| 1 | Registrar valores | `registrarDatos()` | Pide 4 valores y los guarda en la lista. Valida negativos. |
| 2 | Consultar valores | `consultarDatos()` | Muestra cuadrícula AC/HO y SO/ACU. |
| 3 | Actualizar categoría | `actualizarCategoria()` | Modifica una categoría. Valida rango y negativos. |
| 4 | Comparar afinidades | `compararAfinidades()` | Muestra categoría con valor más alto y más bajo usando `for`. |
| 5 | Guardar/cargar datos | `guardarCargarDatos()` | Sub-menú: guarda en archivo o carga desde archivo. Valida existencia y negativos. |
| 6 | Clasificar categoría | `clasificarCategoria()` | Clasifica: <3 Bajo, 3-7 Moderado, >7 Alto. |
| 7 | Comparar estudiantes | `compararConPerfiles()` | Compara contra 5 perfiles hardcodeados, muestra el más afín. |
| 8 | Duplicar valores | `duplicarValores()` | Multiplica todo por 2 con `for`. |
| 9 | Cambio aleatorio | `cambioAleatorio()` | Aumenta o disminuye una categoría al azar. No baja de 0. |
| 10 | Graficar perfil | `graficar()` | Gráfica de barras con matplotlib y colores. |
| 11 | Salir | — | Termina el programa. |

## Requisitos de Entrega 2 cumplidos

1. **Lista** — `perfil = [0, 0, 0, 0]` con 4 posiciones
2. **Funciones** — Cada opción en función independiente
3. **Funcionalidades completas** — 11 opciones operativas
4. **Cuadrícula** — Formato AC/HO y SO/ACU con líneas
5. **Validación** — No negativos en registrar, actualizar y cargar
6. **Duplicar con for** — `for i in range(len(perfil))`
7. **Carga desde archivo** — Lee archivo separado por comas, valida existencia con `os.path.exists()`
8. **Gráfica matplotlib** — Barras con colores, etiquetas y título

## Guía para la sustentación

### Conceptos clave que pueden preguntar

- **Lista `perfil`**: posición 0=Académicos, 1=Hobbies, 2=Sociales, 3=Actividades
- **`for` vs `while`**: el menú usa `while True`, la duplicación usa `for`
- **`range(1, 4)`**: genera 1, 2, 3 (no incluye el 4)
- **`perfil[cat - 1]`**: el usuario ingresa 1-4 pero la lista es 0-3
- **`diff * -1`**: convierte un número negativo en positivo (valor absoluto manual)
- **`os.path.exists()`**: verifica si un archivo existe antes de abrirlo
- **`archivo.split(",")`**: separa el texto del archivo por comas en una lista
- **`random.randint(0, 3)`**: genera un número aleatorio entre 0 y 3 (inclusive)

### Posibles modificaciones en vivo

- Cambiar los rangos de clasificación (ej: <2, 2-5, >5)
- Agregar una 5ta categoría al perfil
- Cambiar la gráfica de barras a dispersión (`plt.scatter`)
- Agregar validación de máximo (ej: no más de 15)
- Modificar los perfiles hardcodeados

### Perfiles hardcodeados (para explicar la comparación)

| Estudiante | AC | HO | SO | ACU |
|------------|----|----|----|----|
| Ana | 5 | 3 | 7 | 4 |
| Carlos | 2 | 6 | 4 | 5 |
| Lucía | 8 | 2 | 5 | 3 |
| Mateo | 4 | 7 | 3 | 6 |
| Sofía | 6 | 4 | 6 | 2 |

La función `compararConPerfiles()` calcula la **diferencia total** (suma de diferencias absolutas en las 4 categorías) entre el usuario y cada perfil. El de menor diferencia es el más afín.

### Estructuras usadas por tema de clase

| Tema | Dónde se usa |
|------|-------------|
| Variables y tipos | `perfil`, `nombresCategorias`, `int()`, `str()` |
| Entrada y salida | `input()`, `print()` en todo el código |
| Condicionales simples | `if` en validaciones de negativos |
| Condicionales múltiples | `if/elif/else` en el menú y clasificación |
| Ciclo `while` | Menú principal `while True` con `break` |
| Textos | Concatenación con `+`, `str()`, `split(",")` |
| Listas | `perfil[0]`, `perfilesEstudiantes[i][j]`, `range(len())` |
| Funciones | 10 funciones independientes |
| Acumuladores y `for` | `diferencia = diferencia + diff`, duplicar valores |
| Archivos | `open()`, `.read()`, `.write()`, `.close()` |
| Librerías | `matplotlib.pyplot`, `random`, `os` |
