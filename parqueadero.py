"""
Programa: parqueadero
Autores: Daniel Felipe Santamaria y Jhosthynn Alexander Sarmiento (era con un compañero anterior en básica)
Fecha: 28 enero 2025.
"""

import os
import time
from datetime import datetime
from enum import Enum


# =========================
# COLORES ANSI
# =========================
RESET = "\033[0m"
AMARILLO = "\033[33m"
VERDE = "\033[32m"
GRIS = "\033[37m"
AZUL_CLARO = "\033[94m"
ROJO = "\033[31m"


# =========================
# FUNCIONES AUXILIARES
# =========================
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def string_to_upper(texto):
    return texto.upper()


def es_bisiesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


# =========================
# ENUM TIPO VEHICULO
# =========================
class TipoVehiculo(Enum):
    CARRO = 1
    MOTO = 2


# =========================
# CLASE USUARIO
# =========================
class Usuario:
    def __init__(self, nombre_completo, identificacion):
        self.nombre_completo = nombre_completo
        self.identificacion = identificacion


# =========================
# CLASE VEHICULO
# =========================
class Vehiculo:
    def __init__(
        self,
        matricula,
        color,
        marca,
        modelo,
        propietario,
        tipo,
        hora_entrada,
    ):
        self.matricula = matricula
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario
        self.tipo = tipo
        self.hora_entrada = hora_entrada
        self.es_recurrente = False

    def calcular_tiempo_estacionado(self, hora_salida):
        diferencia = hora_salida - self.hora_entrada
        return diferencia.total_seconds() / 3600

    def marcar_como_recurrente(self):
        self.es_recurrente = True

    def tipo_vehiculo_to_string(self):
        return "Carro" if self.tipo == TipoVehiculo.CARRO else "Moto"

    def hora_entrada_to_string(self):
        return self.hora_entrada.strftime("%d/%m/%Y %H:%M")


# =========================
# CLASE PARQUEADERO
# =========================
class Parqueadero:
    def __init__(
        self,
        tarifa_carro=8000.0,
        tarifa_moto=4000.0,
        archivo="parqueadero.txt",
    ):
        self.vehiculos = []
        self.historial_vehiculos = []

        self.tarifa_por_hora_carro = tarifa_carro
        self.tarifa_por_hora_moto = tarifa_moto

        self.archivo_datos = archivo

    # =========================
    # UTILIDADES
    # =========================
    def dibujar_linea(self, ancho=80, caracter="-"):
        print(caracter * ancho)

    def centrar_texto(self, texto, ancho=80):
        print(texto.center(ancho))

    # =========================
    # TABLA PRECIOS
    # =========================
    def mostrar_tabla_precios(self):
        self.dibujar_linea()

        self.centrar_texto(VERDE + "TABLA DE PRECIOS" + RESET)

        self.dibujar_linea()

        print(
            f"{GRIS}Tarifa por hora (Carro): {RESET}"
            f"${self.tarifa_por_hora_carro:.2f} COP"
        )

        print(
            f"{GRIS}Tarifa por minuto (Carro): {RESET}"
            f"${self.tarifa_por_hora_carro / 60:.2f} COP"
        )

        print(
            f"{GRIS}Tarifa por hora (Moto): {RESET}"
            f"${self.tarifa_por_hora_moto:.2f} COP"
        )

        print(
            f"{GRIS}Tarifa por minuto (Moto): {RESET}"
            f"${self.tarifa_por_hora_moto / 60:.2f} COP"
        )

        print(f"{GRIS}Descuento recurrente: {RESET}10%")

        print(
            f"{AMARILLO}"
            f"-> Obtenga el descuento si el vehiculo ya ha estado en el parqueadero!"
            f"{RESET}"
        )

        self.dibujar_linea()

    # =========================
    # VALIDACIONES
    # =========================
    def validar_matricula(self, matricula, tipo):
        matricula = matricula.upper()

        if tipo == TipoVehiculo.CARRO:

            if len(matricula) != 6:
                return False

            letras = matricula[:3]
            numeros = matricula[3:]

            return letras.isalpha() and numeros.isdigit()

        else:

            if len(matricula) != 6:
                return False

            letras = matricula[:3]
            numeros = matricula[3:5]
            ultima = matricula[5]

            return (
                letras.isalpha()
                and numeros.isdigit()
                and ultima.isalpha()
            )

    def validar_modelo(self, modelo):
        ano_actual = datetime.now().year
        return 1900 <= modelo <= ano_actual + 1

    def validar_dia(self, mes, dia, ano):

        dias_mes = {
            1: 31,
            2: 29 if es_bisiesto(ano) else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        return 1 <= dia <= dias_mes[mes]

    # =========================
    # LEER FECHA
    # =========================
    def leer_fecha_hora(self):

        ano = datetime.now().year

        while True:
            mes = int(input("Ingrese el mes (MM): "))

            if 1 <= mes <= 12:
                break

            print(ROJO + "Mes invalido." + RESET)

        while True:
            dia = int(input("Ingrese el dia (DD): "))

            if self.validar_dia(mes, dia, ano):
                break

            print(ROJO + "Dia invalido." + RESET)

        while True:
            hora = int(input("Ingrese la hora (HH): "))

            if 0 <= hora <= 23:
                break

            print(ROJO + "Hora invalida." + RESET)

        while True:
            minuto = int(input("Ingrese el minuto (MM): "))

            if 0 <= minuto <= 59:
                break

            print(ROJO + "Minuto invalido." + RESET)

        return datetime(ano, mes, dia, hora, minuto)

    # =========================
    # BUSCAR VEHICULO
    # =========================
    def buscar_vehiculo_historial(self, matricula):

        for vehiculo in self.historial_vehiculos:

            if vehiculo.matricula.upper() == matricula.upper():
                return vehiculo

        return None

    def matricula_en_uso(self, matricula):

        for vehiculo in self.vehiculos:

            if vehiculo.matricula.upper() == matricula.upper():
                return True

        return False

    # =========================
    # REGISTRAR ENTRADA
    # =========================
    def registrar_entrada(self):

        print("Seleccione el tipo de vehiculo:")
        print("1. Carro")
        print("2. Moto")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            tipo = TipoVehiculo.CARRO
        elif opcion == "2":
            tipo = TipoVehiculo.MOTO
        else:
            print(ROJO + "Opcion invalida." + RESET)
            return

        matricula = input("Ingrese la matricula: ")

        if not self.validar_matricula(matricula, tipo):
            print(ROJO + "Matricula invalida." + RESET)
            return

        if self.matricula_en_uso(matricula):
            print(ROJO + "La matricula ya esta registrada." + RESET)
            return

        vehiculo_historial = self.buscar_vehiculo_historial(matricula)

        cargar = False

        if vehiculo_historial:

            print("Vehiculo encontrado en historial.")

            cargar = input(
                "Desea cargar los datos automaticamente? (s/n): "
            ).lower() == "s"

        if cargar:

            color = vehiculo_historial.color
            marca = vehiculo_historial.marca
            modelo = vehiculo_historial.modelo
            propietario = vehiculo_historial.propietario

        else:

            color = input("Ingrese color: ")
            marca = input("Ingrese marca: ")

            while True:

                modelo = int(input("Ingrese modelo: "))

                if self.validar_modelo(modelo):
                    break

                print(ROJO + "Modelo invalido." + RESET)

            nombre = input("Ingrese nombre propietario: ")
            identificacion = input("Ingrese identificacion: ")

            propietario = Usuario(nombre, identificacion)

        print("Ingrese fecha y hora de entrada")

        hora_entrada = self.leer_fecha_hora()

        nuevo = Vehiculo(
            matricula,
            color,
            marca,
            modelo,
            propietario,
            tipo,
            hora_entrada,
        )

        if vehiculo_historial:
            nuevo.marcar_como_recurrente()

            print(
                VERDE
                + "Vehiculo recurrente detectado. Aplicando descuento."
                + RESET
            )

        self.vehiculos.append(nuevo)
        self.historial_vehiculos.append(nuevo)

        print(VERDE + "Vehiculo registrado correctamente." + RESET)

    # =========================
    # CALCULAR COSTO
    # =========================
    def calcular_costo_total(self, vehiculo, hora_salida):

        horas = vehiculo.calcular_tiempo_estacionado(hora_salida)

        tarifa = (
            self.tarifa_por_hora_carro
            if vehiculo.tipo == TipoVehiculo.CARRO
            else self.tarifa_por_hora_moto
        )

        return horas * tarifa

    # =========================
    # REGISTRAR SALIDA
    # =========================
    def registrar_salida(self):

        matricula = input("Ingrese la matricula: ")

        for vehiculo in self.vehiculos:

            if vehiculo.matricula.upper() == matricula.upper():

                print("Ingrese fecha y hora de salida")

                hora_salida = self.leer_fecha_hora()

                if hora_salida < vehiculo.hora_entrada:

                    print(
                        ROJO
                        + "La fecha de salida no puede ser anterior."
                        + RESET
                    )

                    return

                tiempo = vehiculo.calcular_tiempo_estacionado(
                    hora_salida
                )

                costo = self.calcular_costo_total(
                    vehiculo,
                    hora_salida,
                )

                descuento = 0
                total = costo

                if vehiculo.es_recurrente:

                    descuento = costo * 0.10
                    total *= 0.90

                    print(
                        VERDE
                        + "Aplicando descuento del 10%."
                        + RESET
                    )

                print(VERDE + "\n--- FACTURA ---" + RESET)

                print(f"Matricula: {vehiculo.matricula}")
                print(f"Modelo: {vehiculo.modelo}")

                print(f"Tiempo estacionado: {tiempo:.2f} horas")

                print(f"Costo sin descuento: ${costo:.2f}")

                print(f"Descuento: ${descuento:.2f}")

                print(AZUL_CLARO + "---------------------" + RESET)

                print(f"TOTAL A PAGAR: ${total:.2f}")

                print(AZUL_CLARO + "---------------------" + RESET)

                self.vehiculos.remove(vehiculo)

                print(VERDE + "Salida registrada." + RESET)

                return

        print(ROJO + "Vehiculo no encontrado." + RESET)

    # =========================
    # MOSTRAR VEHICULOS
    # =========================
    def mostrar_cantidad_vehiculos(self):

        print(
            f"Cantidad de vehiculos estacionados: {len(self.vehiculos)}"
        )

        if not self.vehiculos:
            print("No hay vehiculos.")
            return

        print(VERDE + "\n--- VEHICULOS ---" + RESET)

        for i, vehiculo in enumerate(self.vehiculos, start=1):

            print(f"\nVehiculo {i}")

            print(f"Tipo: {vehiculo.tipo_vehiculo_to_string()}")

            print(f"Placa: {vehiculo.matricula}")

            print(f"Modelo: {vehiculo.modelo}")

            print(f"Color: {vehiculo.color}")

            print(f"Desde: {vehiculo.hora_entrada_to_string()}")

    # =========================
    # GUARDAR DATOS
    # =========================
    def guardar_datos(self):

        with open(self.archivo_datos, "w", encoding="utf-8") as archivo:

            for vehiculo in self.historial_vehiculos:

                archivo.write(
                    f"{vehiculo.matricula};"
                    f"{vehiculo.color};"
                    f"{vehiculo.marca};"
                    f"{vehiculo.modelo};"
                    f"{vehiculo.propietario.nombre_completo};"
                    f"{vehiculo.propietario.identificacion};"
                    f"{vehiculo.tipo_vehiculo_to_string()};"
                    f"{vehiculo.es_recurrente};"
                    f"{vehiculo.hora_entrada_to_string()}\n"
                )

        print(VERDE + "Datos guardados correctamente." + RESET)

    # =========================
    # CARGAR DATOS
    # =========================
    def cargar_datos(self):

        try:

            with open(self.archivo_datos, "r", encoding="utf-8") as archivo:

                for linea in archivo:

                    datos = linea.strip().split(";")

                    if len(datos) != 9:
                        continue

                    (
                        matricula,
                        color,
                        marca,
                        modelo,
                        nombre,
                        identificacion,
                        tipo,
                        recurrente,
                        fecha,
                    ) = datos

                    propietario = Usuario(nombre, identificacion)

                    tipo_vehiculo = (
                        TipoVehiculo.CARRO
                        if tipo == "Carro"
                        else TipoVehiculo.MOTO
                    )

                    hora_entrada = datetime.strptime(
                        fecha,
                        "%d/%m/%Y %H:%M",
                    )

                    vehiculo = Vehiculo(
                        matricula,
                        color,
                        marca,
                        int(modelo),
                        propietario,
                        tipo_vehiculo,
                        hora_entrada,
                    )

                    vehiculo.es_recurrente = recurrente == "True"

                    self.historial_vehiculos.append(vehiculo)

            print(VERDE + "Datos cargados correctamente." + RESET)

        except FileNotFoundError:

            print(
                ROJO
                + "No existe archivo de datos. Se creara uno nuevo."
                + RESET
            )


# =========================
# MAIN
# =========================
def main():

    parqueadero = Parqueadero()

    parqueadero.cargar_datos()

    while True:

        limpiar_pantalla()

        parqueadero.centrar_texto(
            AZUL_CLARO + "--- MENU PARQUEADERO ---" + RESET
        )

        print("1. Mostrar tabla de precios")
        print("2. Registrar entrada de vehiculo")
        print("3. Registrar salida de vehiculo")
        print("4. Mostrar vehiculos estacionados")
        print("0. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":

            parqueadero.mostrar_tabla_precios()

        elif opcion == "2":

            parqueadero.registrar_entrada()

        elif opcion == "3":

            parqueadero.registrar_salida()

        elif opcion == "4":

            parqueadero.mostrar_cantidad_vehiculos()

        elif opcion == "0":

            parqueadero.guardar_datos()

            print(AMARILLO + "Saliendo..." + RESET)

            break

        else:

            print(ROJO + "Opcion invalida." + RESET)

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()
