"""
Tests para Campus Connect
Ejecutar con: source venv/bin/activate && pytest test_campus_connect.py -v
"""
import sys
import os
import io
from unittest.mock import patch

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

# ---------------------------------------------------------------------------
# Copia de las funciones del notebook (con nombreUsuario y rango 0-10)
# para poder testear sin bloquear por el while True del .py
# ---------------------------------------------------------------------------

perfil = [0, 0, 0, 0]
nombreUsuario = ""
nombresCategorias = ["Académicos", "Hobbies", "Sociales", "Actividades"]
nombresEstudiantes = ["Ana", "Carlos", "Lucía", "Mateo", "Sofía"]
perfilesEstudiantes = [
    [5, 3, 7, 4],
    [2, 6, 4, 5],
    [8, 2, 5, 3],
    [4, 7, 3, 6],
    [6, 4, 6, 2],
]


def reset():
    """Reinicia el estado global antes de cada test."""
    global perfil, nombreUsuario
    perfil[:] = [0, 0, 0, 0]
    nombreUsuario = ""


def registrarDatos(inputs_list):
    """Versión testable: recibe lista de inputs en vez de input()."""
    global nombreUsuario
    print(" ")
    print("--- REGISTRO DE DATOS ---")
    nombreUsuario = inputs_list[0]
    print("Tu nombre: " + nombreUsuario)
    print("(Ingresa valores entre 0 y 10)")
    acad = int(inputs_list[1])
    hobb = int(inputs_list[2])
    soci = int(inputs_list[3])
    acti = int(inputs_list[4])
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


def consultarDatos():
    print("-------------------------")
    if nombreUsuario != "":
        print("  Usuario: " + nombreUsuario)
        print("-------------------------")
    print("AC: " + str(perfil[0]) + " | HO: " + str(perfil[1]))
    print("-------------------------")
    print("SO: " + str(perfil[2]) + " | ACU: " + str(perfil[3]))
    print("-------------------------")


def actualizarCategoria(cat_str, nuevo_str):
    """Versión testable: recibe cat y nuevo como string."""
    print(" ")
    print("Categorías:")
    print("1) Académicos")
    print("2) Hobbies")
    print("3) Sociales")
    print("4) Actividades")
    cat = int(cat_str)
    if cat >= 1 and cat <= 4:
        print("(Valor entre 0 y 10)")
        nuevo = int(nuevo_str)
        if nuevo < 0 or nuevo > 10:
            print("Error: El valor debe estar entre 0 y 10.")
        else:
            perfil[cat - 1] = nuevo
            print("Categoría actualizada correctamente.")
    else:
        print("Categoría incorrecta.")


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


def guardarDatos(nombre_archivo):
    """Guarda perfil + nombre en archivo."""
    archivo = open(nombre_archivo, "w")
    linea = nombreUsuario + "," + str(perfil[0]) + "," + str(perfil[1]) + "," + str(perfil[2]) + "," + str(perfil[3])
    archivo.write(linea)
    archivo.close()
    print("Datos guardados en " + nombre_archivo)


def cargarDatos(nombre_archivo):
    """Carga perfil + nombre desde archivo."""
    global nombreUsuario
    if os.path.exists(nombre_archivo):
        archivo = open(nombre_archivo, "r")
        contenido = archivo.read()
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
            print("Datos cargados desde " + nombre_archivo + " para " + nombreUsuario)
        archivo.close()
    else:
        print("Error: El archivo " + nombre_archivo + " no existe.")


def clasificarCategoria(cat_str):
    """Versión testable."""
    print(" ")
    print("Categorías:")
    print("1) Académicos")
    print("2) Hobbies")
    print("3) Sociales")
    print("4) Actividades")
    cat = int(cat_str)
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


def duplicarValores():
    for i in range(len(perfil)):
        perfil[i] = perfil[i] * 2
    print("Valores duplicados correctamente.")


def cambioAleatorio(seed_val):
    """Versión testable con seed fijo."""
    random.seed(seed_val)
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
    plt.close()


# ===========================================================================
# TESTS
# ===========================================================================

class TestRegistrarDatos:
    """FUNCIÓN 1: Registrar datos."""

    def setup_method(self):
        reset()

    def test_registro_normal(self, capsys):
        registrarDatos(["Paula", "5", "3", "7", "2"])
        assert perfil == [5, 3, 7, 2]
        assert nombreUsuario == "Paula"
        out = capsys.readouterr().out
        assert "Perfil registrado correctamente para Paula." in out

    def test_registro_valores_cero(self, capsys):
        registrarDatos(["Ana", "0", "0", "0", "0"])
        assert perfil == [0, 0, 0, 0]

    def test_registro_maximo(self, capsys):
        registrarDatos(["Luis", "10", "10", "10", "10"])
        assert perfil == [10, 10, 10, 10]

    def test_registro_nombre_guardado(self):
        registrarDatos(["María", "1", "2", "3", "4"])
        assert nombreUsuario == "María"

    def test_registro_negativos_no_actualiza(self, capsys):
        registrarDatos(["Test", "-1", "3", "5", "2"])
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "negativos" in out

    def test_registro_mayor_10_no_actualiza(self, capsys):
        registrarDatos(["Test", "11", "3", "5", "2"])
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "entre 0 y 10" in out

    def test_registro_mixto_invalido(self, capsys):
        registrarDatos(["Test", "5", "15", "3", "2"])
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "entre 0 y 10" in out

    def test_registro_rango_aclarado(self, capsys):
        registrarDatos(["Test", "1", "2", "3", "4"])
        out = capsys.readouterr().out
        assert "(Ingresa valores entre 0 y 10)" in out


class TestConsultarDatos:
    """FUNCIÓN 2: Consultar datos."""

    def setup_method(self):
        reset()

    def test_consultar_perfil_vacio(self, capsys):
        consultarDatos()
        out = capsys.readouterr().out
        assert "AC: 0 | HO: 0" in out
        assert "SO: 0 | ACU: 0" in out

    def test_consultar_perfil_con_datos(self, capsys):
        perfil[:] = [5, 3, 7, 2]
        consultarDatos()
        out = capsys.readouterr().out
        assert "AC: 5 | HO: 3" in out
        assert "SO: 7 | ACU: 2" in out

    def test_consultar_muestra_nombre(self, capsys):
        global nombreUsuario
        nombreUsuario = "Paula"
        perfil[:] = [4, 6, 3, 2]
        consultarDatos()
        out = capsys.readouterr().out
        assert "Usuario: Paula" in out

    def test_consultar_sin_nombre_no_muestra_usuario(self, capsys):
        consultarDatos()
        out = capsys.readouterr().out
        assert "Usuario:" not in out


class TestActualizarCategoria:
    """FUNCIÓN 3: Actualizar categoría."""

    def setup_method(self):
        reset()

    def test_actualizar_academicos(self, capsys):
        actualizarCategoria("1", "8")
        assert perfil[0] == 8
        out = capsys.readouterr().out
        assert "actualizada correctamente" in out

    def test_actualizar_hobbies(self, capsys):
        actualizarCategoria("2", "5")
        assert perfil[1] == 5

    def test_actualizar_sociales(self, capsys):
        actualizarCategoria("3", "3")
        assert perfil[2] == 3

    def test_actualizar_actividades(self, capsys):
        actualizarCategoria("4", "7")
        assert perfil[3] == 7

    def test_actualizar_categoria_0(self, capsys):
        actualizarCategoria("0", "5")
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "incorrecta" in out

    def test_actualizar_categoria_5(self, capsys):
        actualizarCategoria("5", "5")
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "incorrecta" in out

    def test_actualizar_valor_negativo(self, capsys):
        actualizarCategoria("1", "-3")
        assert perfil[0] == 0
        out = capsys.readouterr().out
        assert "entre 0 y 10" in out

    def test_actualizar_valor_11(self, capsys):
        actualizarCategoria("2", "11")
        assert perfil[1] == 0
        out = capsys.readouterr().out
        assert "entre 0 y 10" in out

    def test_actualizar_valor_limite_10(self, capsys):
        actualizarCategoria("1", "10")
        assert perfil[0] == 10

    def test_actualizar_rango_aclarado(self, capsys):
        actualizarCategoria("1", "5")
        out = capsys.readouterr().out
        assert "(Valor entre 0 y 10)" in out


class TestCompararAfinidades:
    """FUNCIÓN 4: Comparar afinidades."""

    def setup_method(self):
        reset()

    def test_mayor_y_menor(self, capsys):
        perfil[:] = [2, 8, 5, 1]
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Mayor afinidad: Hobbies (8)" in out
        assert "Menor afinidad: Actividades (1)" in out

    def test_todos_iguales(self, capsys):
        perfil[:] = [5, 5, 5, 5]
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Mayor afinidad: Académicos (5)" in out
        assert "Menor afinidad: Académicos (5)" in out

    def test_todos_cero(self, capsys):
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Mayor afinidad: Académicos (0)" in out
        assert "Menor afinidad: Académicos (0)" in out

    def test_primer_valor_mayor(self, capsys):
        perfil[:] = [9, 2, 3, 1]
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Mayor afinidad: Académicos (9)" in out

    def test_ultimo_valor_menor(self, capsys):
        perfil[:] = [7, 6, 5, 0]
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Menor afinidad: Actividades (0)" in out


class TestGuardarCargarDatos:
    """FUNCIÓN 5: Guardar / cargar datos."""

    def setup_method(self):
        reset()

    def test_guardar_y_cargar(self, capsys, tmp_path):
        global nombreUsuario
        nombreUsuario = "Paula"
        perfil[:] = [4, 6, 3, 2]
        archivo = str(tmp_path / "test_perfil.txt")

        guardarDatos(archivo)
        assert os.path.exists(archivo)

        reset()
        cargarDatos(archivo)
        assert perfil == [4, 6, 3, 2]
        assert nombreUsuario == "Paula"
        out = capsys.readouterr().out
        assert "Datos cargados" in out

    def test_cargar_archivo_no_existente(self, capsys):
        cargarDatos("archivo_inexistente_xyz.txt")
        out = capsys.readouterr().out
        assert "no existe" in out

    def test_guardar_incluye_nombre(self, tmp_path):
        global nombreUsuario
        nombreUsuario = "María"
        perfil[:] = [1, 2, 3, 4]
        archivo = str(tmp_path / "test2.txt")

        guardarDatos(archivo)
        with open(archivo, "r") as f:
            contenido = f.read()
        assert contenido == "María,1,2,3,4"

    def test_cargar_restaura_nombre(self, tmp_path):
        global nombreUsuario
        nombreUsuario = "Carlos"
        perfil[:] = [7, 8, 9, 10]
        archivo = str(tmp_path / "test3.txt")

        guardarDatos(archivo)
        reset()
        cargarDatos(archivo)
        assert nombreUsuario == "Carlos"

    def test_cargar_valores_negativos_no_actualiza(self, capsys, tmp_path):
        archivo = str(tmp_path / "neg.txt")
        with open(archivo, "w") as f:
            f.write("Test,-1,2,3,4")
        cargarDatos(archivo)
        assert perfil == [0, 0, 0, 0]
        out = capsys.readouterr().out
        assert "negativos" in out

    def test_cargar_valores_cero(self, tmp_path):
        archivo = str(tmp_path / "ceros.txt")
        with open(archivo, "w") as f:
            f.write("Test,0,0,0,0")
        cargarDatos(archivo)
        assert perfil == [0, 0, 0, 0]


class TestClasificarCategoria:
    """FUNCIÓN 6: Clasificar categoría."""

    def setup_method(self):
        reset()

    def test_bajo_nivel(self, capsys):
        perfil[:] = [1, 0, 2, 5]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Bajo nivel" in out

    def test_moderado_nivel(self, capsys):
        perfil[:] = [5, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Moderado nivel" in out

    def test_alto_nivel(self, capsys):
        perfil[:] = [9, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Alto nivel" in out

    def test_limite_bajo_2(self, capsys):
        perfil[:] = [2, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Bajo nivel" in out

    def test_limite_moderado_3(self, capsys):
        perfil[:] = [3, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Moderado nivel" in out

    def test_limite_moderado_7(self, capsys):
        perfil[:] = [7, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Moderado nivel" in out

    def test_limite_alto_8(self, capsys):
        perfil[:] = [8, 0, 0, 0]
        clasificarCategoria("1")
        out = capsys.readouterr().out
        assert "Alto nivel" in out

    def test_categoria_invalida_0(self, capsys):
        clasificarCategoria("0")
        out = capsys.readouterr().out
        assert "incorrecta" in out

    def test_categoria_invalida_5(self, capsys):
        clasificarCategoria("5")
        out = capsys.readouterr().out
        assert "incorrecta" in out

    def test_todas_categorias(self, capsys):
        perfil[:] = [1, 5, 9, 3]
        for cat in ["1", "2", "3", "4"]:
            clasificarCategoria(cat)
        out = capsys.readouterr().out
        assert "Bajo nivel" in out
        assert "Moderado nivel" in out
        assert "Alto nivel" in out


class TestCompararConPerfiles:
    """FUNCIÓN 7: Comparar con otros estudiantes."""

    def setup_method(self):
        reset()

    def test_afinidad_con_ana(self, capsys):
        # Perfil idéntico a Ana → diferencia 0
        perfil[:] = [5, 3, 7, 4]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Ana" in out
        assert "0" in out

    def test_afinidad_con_carlos(self, capsys):
        # Perfil idéntico a Carlos → diferencia 0
        perfil[:] = [2, 6, 4, 5]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Carlos" in out

    def test_afinidad_con_lucia(self, capsys):
        perfil[:] = [8, 2, 5, 3]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Lucía" in out

    def test_muestra_nombre_usuario(self, capsys):
        global nombreUsuario
        nombreUsuario = "Paula"
        perfil[:] = [5, 3, 7, 4]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Paula, tienes más afinidad" in out

    def test_sin_nombre_usuario(self, capsys):
        perfil[:] = [5, 3, 7, 4]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Tienes más afinidad" in out

    def test_perfil_vacio(self, capsys):
        perfil[:] = [0, 0, 0, 0]
        compararConPerfiles()
        out = capsys.readouterr().out
        # Debería encontrar al más cercano
        assert "afinidad" in out
        assert "Diferencia total:" in out

    def test_muestra_diferencia(self, capsys):
        perfil[:] = [5, 3, 7, 4]
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "Diferencia total: 0" in out


class TestDuplicarValores:
    """FUNCIÓN 8: Duplicar valores."""

    def setup_method(self):
        reset()

    def test_duplicar_normal(self, capsys):
        perfil[:] = [2, 4, 3, 1]
        duplicarValores()
        assert perfil == [4, 8, 6, 2]
        out = capsys.readouterr().out
        assert "duplicados" in out

    def test_duplicar_ceros(self, capsys):
        duplicarValores()
        assert perfil == [0, 0, 0, 0]

    def test_duplicar_dos_veces(self):
        perfil[:] = [1, 2, 3, 4]
        duplicarValores()
        duplicarValores()
        assert perfil == [4, 8, 12, 16]

    def test_duplicar_maximos(self):
        perfil[:] = [10, 10, 10, 10]
        duplicarValores()
        assert perfil == [20, 20, 20, 20]

    def test_duplicar_un_valor(self):
        perfil[:] = [5, 0, 0, 0]
        duplicarValores()
        assert perfil == [10, 0, 0, 0]


class TestCambioAleatorio:
    """FUNCIÓN 9: Cambio aleatorio."""

    def setup_method(self):
        reset()

    def test_aumenta_en_1(self, capsys):
        perfil[:] = [5, 5, 5, 5]
        original = perfil[:]
        cambioAleatorio(seed_val=42)
        total_original = sum(original)
        total_nuevo = sum(perfil)
        assert total_nuevo == total_original + 1 or total_nuevo == total_original - 1
        out = capsys.readouterr().out
        assert "aumentó" in out or "disminuyó" in out

    def test_no_disminuye_debajo_cero(self, capsys):
        perfil[:] = [0, 0, 0, 0]
        cambioAleatorio(seed_val=42)
        for v in perfil:
            assert v >= 0

    def test_cambio_modifica_solo_una_categoria(self):
        perfil[:] = [5, 5, 5, 5]
        cambioAleatorio(seed_val=7)
        cambios = sum(1 for i in range(4) if perfil[i] != 5)
        assert cambios == 1

    def test_multiple_seed_no_negativos(self):
        perfil[:] = [1, 0, 2, 0]
        for seed in range(50):
            reset()
            perfil[:] = [1, 0, 2, 0]
            cambioAleatorio(seed_val=seed)
            for v in perfil:
                assert v >= 0, f"Seed {seed} produjo valor negativo: {perfil}"


class TestGraficar:
    """FUNCIÓN 10: Graficar perfil."""

    def setup_method(self):
        reset()

    def test_graficar_sin_error(self, capsys):
        perfil[:] = [4, 6, 3, 2]
        graficar()  # No debe lanzar excepción

    def test_graficar_con_nombre(self, capsys):
        global nombreUsuario
        nombreUsuario = "Paula"
        perfil[:] = [2, 6, 3, 2]
        graficar()

    def test_graficar_ceros(self):
        graficar()

    def test_graficar_maximos(self):
        perfil[:] = [10, 10, 10, 10]
        graficar()


class TestIntegracion:
    """Tests de integración: flujos completos."""

    def setup_method(self):
        reset()

    def test_flujo_completo(self, capsys, tmp_path):
        """Registrar → consultar → actualizar → guardar → cargar → comparar."""
        global nombreUsuario

        # 1. Registrar
        registrarDatos(["María", "4", "6", "3", "2"])
        assert nombreUsuario == "María"
        assert perfil == [4, 6, 3, 2]

        # 2. Consultar
        consultarDatos()
        out = capsys.readouterr().out
        assert "Usuario: María" in out
        assert "AC: 4 | HO: 6" in out

        # 3. Actualizar
        actualizarCategoria("1", "8")
        assert perfil[0] == 8

        # 4. Guardar
        archivo = str(tmp_path / "integra.txt")
        guardarDatos(archivo)

        # 5. Reset y cargar
        reset()
        cargarDatos(archivo)
        assert nombreUsuario == "María"
        assert perfil == [8, 6, 3, 2]

        # 6. Comparar afinidades
        compararAfinidades()
        out = capsys.readouterr().out
        assert "Mayor afinidad: Hobbies" in out or "Mayor afinidad: Académicos" in out

        # 7. Comparar con otros
        compararConPerfiles()
        out = capsys.readouterr().out
        assert "María, tienes más afinidad" in out

    def test_flujo_duplicar_y_clasificar(self, capsys):
        registrarDatos(["Test", "2", "1", "3", "4"])
        duplicarValores()
        assert perfil == [4, 2, 6, 8]

        clasificarCategoria("1")  # 4 → moderado
        out = capsys.readouterr().out
        assert "Moderado" in out

    def test_flujo_guardar_cargar_preserva_estado(self, tmp_path):
        global nombreUsuario
        registrarDatos(["Carlos", "7", "3", "5", "9"])

        archivo = str(tmp_path / "estado.txt")
        guardarDatos(archivo)

        # Simular otra sesión
        reset()
        assert perfil == [0, 0, 0, 0]
        assert nombreUsuario == ""

        cargarDatos(archivo)
        assert perfil == [7, 3, 5, 9]
        assert nombreUsuario == "Carlos"
