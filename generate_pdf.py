from fpdf import FPDF

class CheatSheet(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, "Campus Connect - Cheat Sheet Sustentacion", align="C", new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-10)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 5, f"Pagina {self.page_no()}/{{nb}}", align="C")

    def section(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_fill_color(33, 150, 243)
        self.set_text_color(255, 255, 255)
        self.cell(0, 7, f"  {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def subsection(self, title):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(33, 100, 180)
        self.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self.set_font("Helvetica", "", 8)
        self.multi_cell(0, 4, text)
        self.ln(1)

    def code(self, text):
        self.set_font("Courier", "", 7.5)
        self.set_fill_color(240, 240, 240)
        self.multi_cell(0, 3.8, text, fill=True)
        self.set_font("Helvetica", "", 8)
        self.ln(1)

    def row(self, cols, widths, bold=False, fill=False):
        style = "B" if bold else ""
        self.set_font("Helvetica", style, 7.5)
        if fill:
            self.set_fill_color(230, 240, 255)
        for i, (col, w) in enumerate(zip(cols, widths)):
            self.cell(w, 4.5, f" {col}", border=1, fill=fill,
                     new_x="RIGHT", new_y="TOP")
        self.ln()


pdf = CheatSheet()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()
pdf.set_margins(10, 10, 10)

# ========== PORTADA ==========
pdf.set_font("Helvetica", "B", 20)
pdf.ln(25)
pdf.cell(0, 10, "Campus Connect", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 7, "Cheat Sheet - Sustentacion Entrega 2", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_font("Helvetica", "", 10)
pdf.cell(0, 6, "Mariluz Botero Gomez  |  Maria Paula Sarralde", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, "Docente: Juan Camilo Saldarriaga", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)

pdf.set_font("Helvetica", "I", 9)
pdf.set_text_color(100, 100, 100)
pdf.multi_cell(0, 5,
    "Este documento resume todo lo que necesitas saber antes de sustentar. "
    "Lleva esto impreso o en el celular como referencia rapida.",
    align="C")
pdf.set_text_color(0, 0, 0)

# ========== ESTRUCTURA DE DATOS ==========
pdf.add_page()
pdf.section("Estructura de datos")
pdf.body("La variable principal es una LISTA con 4 posiciones:")

widths = [15, 40, 135]
pdf.row(["Pos", "Nombre", "Que representa"], widths, bold=True, fill=True)
pdf.row(["0", "Academicos (AC)", "Cantidad de temas de estudio o areas de conocimiento de interes"], widths)
pdf.row(["1", "Hobbies (HO)", "Cantidad de actividades recreativas que hace el estudiante"], widths)
pdf.row(["2", "Sociales (SO)", "Cantidad de preferencias de planes sociales e interaccion"], widths)
pdf.row(["3", "Actividades (ACU)", "Cantidad de clubes, grupos, eventos del campus donde participa"], widths)
pdf.ln(2)
pdf.code("perfil = [0, 0, 0, 0]  # Valores iniciales en cero")
pdf.body("Se accede con perfil[0], perfil[1], perfil[2], perfil[3]. El usuario ingresa 1-4 pero la lista es 0-3, por eso se usa perfil[cat - 1].")

# ========== MENU COMPLETO ==========
pdf.section("Menu de opciones (11 opciones)")
pdf.body("El menu usa un ciclo while True. Cada opcion llama una funcion independiente.")

widths2 = [12, 50, 45, 83]
pdf.row(["#", "Opcion", "Funcion", "Que hace / Estructuras que usa"], widths2, bold=True, fill=True)
pdf.row(["1", "Registrar valores", "registrarDatos()", "Pide 4 valores, valida negativos con if, guarda en lista"], widths2)
pdf.row(["2", "Consultar valores", "consultarDatos()", "Muestra cuadricula AC/HO y SO/ACU con lineas"], widths2)
pdf.row(["3", "Actualizar categoria", "actualizarCategoria()", "Pide numero 1-4, valida rango y negativos"], widths2)
pdf.row(["4", "Comparar afinidades", "compararAfinidades()", "Recorre lista con for, halla mayor y menor"], widths2)
pdf.row(["5", "Guardar/cargar datos", "guardarCargarDatos()", "Sub-menu, escribe/lee archivo, os.path.exists()"], widths2)
pdf.row(["6", "Clasificar categoria", "clasificarCategoria()", "if/elif: <3 Bajo, 3-7 Moderado, >7 Alto"], widths2)
pdf.row(["7", "Comparar estudiantes", "compararConPerfiles()", "Compara contra 5 perfiles con doble for"], widths2)
pdf.row(["8", "Duplicar valores", "duplicarValores()", "Multiplica por 2 con for y range(len(perfil))"], widths2)
pdf.row(["9", "Cambio aleatorio", "cambioAleatorio()", "random.randint(), no baja de 0"], widths2)
pdf.row(["10", "Graficar perfil", "graficar()", "plt.bar() con colores, xlabel, ylabel, title, show"], widths2)
pdf.row(["11", "Salir", "(break)", "Termina el while True"], widths2)

# ========== PERFILES HARDCODEADOS ==========
pdf.ln(2)
pdf.section("Perfiles hardcodeados (5 estudiantes)")
pdf.body("Estan definidos como una lista de listas. Se usan en la opcion 7 para comparar afinidades.")

widths3 = [35, 25, 25, 25, 25, 55]
pdf.row(["Estudiante", "AC", "HO", "SO", "ACU", "Perfil"], widths3, bold=True, fill=True)
pdf.row(["Ana", "5", "3", "7", "4", "Equilibrada, mas social"], widths3)
pdf.row(["Carlos", "2", "6", "4", "5", "Hobbyista y activo"], widths3)
pdf.row(["Lucia", "8", "2", "5", "3", "Academica, poco hobby"], widths3)
pdf.row(["Mateo", "4", "7", "3", "6", "Hobbyista y actividades"], widths3)
pdf.row(["Sofia", "6", "4", "6", "2", "Academica y social"], widths3)
pdf.ln(2)
pdf.body("Como funciona la comparacion: suma la diferencia absoluta en las 4 categorias. El de menor diferencia total es el mas afin.")
pdf.code("diff = perfil[j] - perfilesEstudiantes[i][j]\nif diff < 0:\n    diff = diff * -1  # Convierte negativo a positivo\n diferencia = diferencia + diff")

# ========== CONCEPTOS CLAVE ==========
pdf.add_page()
pdf.section("Conceptos clave para la sustentacion")

pdf.subsection("1. Por que usamos lista y no variables separadas?")
pdf.body("La Entrega 2 exige usar una lista. Ventajas: se puede recorrer con for, se accede por posicion, permite operaciones masivas como duplicar todo con un solo ciclo.")

pdf.subsection("2. for vs while")
pdf.body("- while True: se usa para el menu porque no sabemos cuantas veces va a repetir el usuario.")
pdf.body("- for: se usa para recorrer la lista (duplicar, comparar) porque sabemos cuantos elementos hay (4 categorias, 5 perfiles).")

pdf.subsection("3. range(1, 4) genera 1, 2, 3 (NO incluye el 4)")
pdf.body("El range en Python no incluye el ultimo numero. range(len(perfil)) genera 0, 1, 2, 3 para una lista de 4 elementos.")

pdf.subsection("4. perfil[cat - 1] - Conversion usuario a indice")
pdf.body("El usuario ingresa 1-4, pero la lista es 0-3. Si el usuario elige categoria 2 (Hobbies), accedemos a perfil[2-1] = perfil[1].")

pdf.subsection("5. diff * -1 - Valor absoluto sin usar abs()")
pdf.body("Si la diferencia es negativa (ej: -3), multiplicar por -1 la convierte en positiva (3). Asi medimos la distancia real entre valores sin importar el orden.")

pdf.subsection("6. os.path.exists() - Verificar si archivo existe")
pdf.body("Antes de abrir un archivo para leer, verificamos que exista. Si no existe, mostramos error en vez de que el programa se caiga.")

pdf.subsection("7. archivo.split(',')")
pdf.body("Lee el archivo como texto '4,6,3,2' y lo convierte en una lista ['4', '6', '3', '2']. Luego convertimos cada elemento a int().")

pdf.subsection("8. %matplotlib inline")
pdf.body("Comando especial de Jupyter para que las graficas se muestren dentro del notebook en vez de abrir una ventana separada.")

pdf.subsection("9. random.randint(0, 3)")
pdf.body("Genera un numero aleatorio entre 0 y 3 (inclusive). Se usa para elegir una categoria al azar en el cambio aleatorio.")

# ========== REQUISITOS ==========
pdf.section("Checklist de requisitos Entrega 2")

widths4 = [10, 55, 75, 50]
pdf.row(["#", "Requisito", "Donde se cumple", "Lineas clave"], widths4, bold=True, fill=True)
pdf.row(["1", "Variables a lista", "perfil = [0, 0, 0, 0]", "4 posiciones: AC, HO, SO, ACU"], widths4)
pdf.row(["2", "Opciones en funciones", "10 funciones def...", "Cada opcion = una funcion"], widths4)
pdf.row(["3", "Funcionalidades completas", "Menu con 11 opciones", "if/elif para cada opcion"], widths4)
pdf.row(["4", "Cuadricula en consulta", "consultarDatos()", "lineas + formato AC/HO"], widths4)
pdf.row(["5", "Validacion no negativos", "registrar, actualizar, cargar", "if val < 0: print error"], widths4)
pdf.row(["6", "Duplicar con for", "duplicarValores()", "for i in range(len(perfil))"], widths4)
pdf.row(["7", "Carga desde archivo", "guardarCargarDatos()", "open, read, split, int"], widths4)
pdf.row(["8", "Grafica matplotlib", "graficar()", "plt.bar() con colores"], widths4)

# ========== VALIDACIONES ==========
pdf.ln(2)
pdf.section("Validaciones implementadas")
pdf.body("El sistema tiene 4 puntos de validacion:")
pdf.body("1. registrarDatos(): si algun valor es negativo, NO se actualiza la lista. Muestra error.")
pdf.body("2. actualizarCategoria(): si el nuevo valor es negativo, NO se actualiza. Muestra error.")
pdf.body("3. guardarCargarDatos() (cargar): si el archivo tiene negativos, NO se actualiza. Muestra error.")
pdf.body("4. cambioAleatorio(): si el valor ya es 0 y toca disminuir, NO baja. Muestra mensaje.")
pdf.body("5. guardarCargarDatos() (cargar): si el archivo no existe, muestra error con os.path.exists().")

# ========== EJEMPLO INTERACCION ==========
pdf.add_page()
pdf.section("Ejemplo completo de interaccion")
pdf.body("Asi debes demostrar el sistema en la sustentacion:")
pdf.ln(1)

steps = [
    ("1. Ejecutar celda de imports", "Muestra 'Librerias importadas correctamente.'"),
    ("2. Ejecutar celda de variables", "Muestra 'Variables inicializadas. Perfil: [0, 0, 0, 0]'"),
    ("3. Ejecutar celda de funciones", "Muestra '10 funciones cargadas correctamente.'"),
    ("4. Ejecutar celda de datos.txt", "Muestra 'Archivo datos.txt creado con valores: 4, 6, 3, 2'"),
    ("5. Ejecutar celda de visualizacion", "Muestra la grafica de barras con datos de ejemplo"),
    ("6. Ejecutar celda del menu", "Aparece el menu interactivo"),
    ("7. Opcion 1: Registrar", "Ingresar: 5, 3, 7, 2  ->  'Perfil registrado correctamente.'"),
    ("8. Opcion 2: Consultar", "Muestra cuadricula con los valores ingresados"),
    ("9. Opcion 4: Comparar", "Muestra 'Mayor: Sociales (7)' y 'Menor: Actividades (2)'"),
    ("10. Opcion 7: Comparar estudiantes", "Muestra con quien tiene mas afinidad"),
    ("11. Opcion 6: Clasificar", "Elegir Hobbies (3) -> 'Moderado nivel de intereses'"),
    ("12. Opcion 8: Duplicar", "Los valores se multiplican por 2"),
    ("13. Opcion 5: Guardar", "Guardar en 'prueba.txt' -> confirmacion"),
    ("14. Opcion 5: Cargar", "Cargar 'prueba.txt' -> datos restaurados"),
    ("15. Opcion 10: Graficar", "Muestra grafica actualizada"),
    ("16. Opcion 11: Salir", "'Hasta pronto!' y termina el programa"),
]

for i, (step, result) in enumerate(steps):
    pdf.set_font("Helvetica", "B", 7.5)
    pdf.cell(60, 4, step)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.cell(0, 4, f"-> {result}", new_x="LMARGIN", new_y="NEXT")

# ========== POSIBLES PREGUNTAS ==========
pdf.ln(3)
pdf.section("Posibles preguntas del docente")

questions = [
    ("Por que uso lista y no variables separadas?",
     "Porque la Entrega 2 lo exige. Ademas, con lista puedo recorrer con for y hacer operaciones masivas como duplicar."),
    ("Que hace range(1, 4)?",
     "Genera los numeros 1, 2 y 3. El range no incluye el ultimo valor."),
    ("Por que perfil[cat - 1]?",
     "Porque el usuario ingresa 1 a 4, pero la lista empieza en 0. Entonces si elige 2, accedo a la posicion 1."),
    ("Como funciona la comparacion con otros estudiantes?",
     "Sumo la diferencia absoluta entre cada categoria del usuario y cada perfil. El de menor diferencia es el mas afin."),
    ("Que pasa si ingreso un valor negativo?",
     "El sistema muestra 'Error: No se permiten valores negativos' y NO actualiza los datos."),
    ("Para que sirve os.path.exists()?",
     "Verifica si un archivo existe antes de intentar leerlo, para que el programa no se caiga."),
    ("Que librerias usa el proyecto?",
     "matplotlib.pyplot para graficar, random para numeros aleatorios, os para verificar archivos."),
    ("Cual es la diferencia entre while y for?",
     "while repite hasta que se cumpla una condicion (menu). for repite un numero conocido de veces (recorrer lista)."),
    ("Que hace split(',')?",
     "Toma un texto como '4,6,3,2' y lo convierte en una lista ['4','6','3','2']."),
    ("Como se guarda la informacion en el archivo?",
     "Se concatenan los 4 valores separados por coma y se escriben con archivo.write()."),
]

for q, a in questions:
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(0, 4.5, f"P: {q}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 4, f"R: {a}")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1)

# ========== POSIBLES MODIFICACIONES EN VIVO ==========
pdf.add_page()
pdf.section("Posibles modificaciones en vivo (< 2 minutos)")
pdf.body("El docente puede pedirte que modifiques algo. Aqui tienes las mas probables con la solucion:")
pdf.ln(1)

mods = [
    ("Cambiar rangos de clasificacion",
     "Actual: <3 Bajo, 3-7 Moderado, >7 Alto.\nNuevo (ejemplo): <2 Bajo, 2-5 Medio, >5 Alto.\n\nCambiar en clasificarCategoria() los valores de los if/elif."),
    ("Agregar validacion de maximo (ej: no mas de 15)",
     "En registrarDatos() o actualizarCategoria(), agregar:\nif acad > 15:\n    print('Error: Maximo 15')\nelse:\n    perfil[0] = acad"),
    ("Cambiar grafica de barras a dispersion",
     "En graficar(), cambiar:\nplt.bar(x, y)  por  plt.scatter(x, y)"),
    ("Agregar una 5ta categoria",
     "1. Cambiar perfil = [0,0,0,0,0]\n2. Agregar nombre a nombresCategorias\n3. Cambiar range(4) por range(5) en compararConPerfiles\n4. Agregar columna a perfilesEstudiantes\n5. Actualizar cuadricula en consultarDatos"),
    ("Mostrar todos los perfiles hardcodeados",
     "Cambiar compararConPerfiles() para que imprima cada diferencia en vez de solo la menor:\nfor i in range(len(perfilesEstudiantes)):\n    print(nombresEstudiantes[i] + ': ' + str(diferencia))"),
    ("Cambiar duplicar por triplicar",
     "En duplicarValores(), cambiar:\nperfil[i] = perfil[i] * 2  por  perfil[i] = perfil[i] * 3"),
]

for title, sol in mods:
    pdf.subsection(title)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.multi_cell(0, 3.8, sol)
    pdf.ln(2)

# ========== TEMAS POR SEMANA ==========
pdf.section("Temas del curso y donde se usan")
pdf.body("Si el docente pregunta 'donde usa X concepto', aqui esta la respuesta rapida:")

widths5 = [55, 135]
pdf.row(["Tema del curso", "Donde se usa en el proyecto"], widths5, bold=True, fill=True)
topics = [
    ("Variables y tipos", "perfil (lista), nombresCategorias (lista), int(), str()"),
    ("Entrada y salida", "input() para pedir datos, print() para mostrar resultados"),
    ("Condicionales simples (if)", "Validacion de negativos: if acad < 0"),
    ("Condicionales multiples", "Menu con if/elif/else, clasificacion Bajo/Moderado/Alto"),
    ("Ciclo while", "Menu principal: while True con break para salir"),
    ("Textos", "Concatenacion con +, str(), split(','), archivo.read()"),
    ("Listas", "perfil[0], perfilesEstudiantes[i][j], range(len())"),
    ("Funciones", "10 funciones: registrarDatos(), consultarDatos(), etc."),
    ("Acumuladores y for", "diferencia = diferencia + diff, duplicarValores()"),
    ("Archivos", "open(), .read(), .write(), .close(), os.path.exists()"),
    ("Librerias (matplotlib)", "plt.bar(), plt.xlabel(), plt.ylabel(), plt.show()"),
]
for topic, where in topics:
    pdf.row([topic, where], widths5)

# ========== OUTPUT
pdf.output("sustentacion_cheatsheet.pdf")
print("PDF generado: sustentacion_cheatsheet.pdf")
