from Busqueda import Competencia
from Compra import main_compra
import random
import string


class Competencia:
    def __init__(self, id, name, stadium, capacity):
        self.id = id
        self.name = name
        self.stadium = stadium
        self.capacity = capacity
        self.taken_seats = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_stadium(self):
        return self.stadium

    def get_capacity(self):
        return self.capacity

    def get_taken_seats(self):
        return self.taken_seats

    def nueva_venta(self):
        self.capacity -= 1

    def nuevo_asiento(self, asiento):
        self.taken_seats.append(asiento)

    def print_partido(self):
        print(f"Partido {self.id}: {self.name} - Estadio {self.stadium}")

def main_compra(lista_estadios, lista_partidos, lista_purchases, codigo_compra):
    partido = escoger_partido(lista_partidos, lista_estadios)
    proceso(lista_partidos, lista_purchases, codigo_compra, partido)

def proceso(lista_partidos, lista_compras, codigo_compra, partido):
    while True:
        try:
            name = input("Ingrese el nombre de usuario: ")
            if not "".join(name.split()).isalpha():
                raise Exception
            break
        except:
            print("Error, datos inválidos. Intente de nuevo")

    while True:
        try:
            id = int(input("Ingrese su identificación: "))
            if id < 0:
                raise Exception
            break
        except:
            print("Error, datos inválidos. Intente de nuevo")

    while True:
        try:
            age = int(input("Ingrese su edad: "))
            if age < 0:
                raise Exception
            break
        except:
            print("Error, datos inválidos. Intente de nuevo")

    partido_escogido = partido
    tipo = escoger_tipo_entrada()
    estadio_escogido = partido_escogido.get_stadium()
    asiento = escoger_asiento(estadio_escogido, tipo, partido_escogido)

    if tipo == "General":
        inicial = "35$"
    else:
        inicial = "75$"

    descuento_por_ser_vampiro = vampire(id)
    if descuento_por_ser_vampiro:
        print(" Descuento por Vampiro!!! (50%)")
        descuento = float(inicial) / 2
    else:
        descuento = 0

    impuesto = float(inicial) * 0.16
    total = float(inicial) + impuesto - descuento

    partido_str = partido_escogido.get_name()
    estadio_str = partido_escogido.get_stadium()

    print("""
    Vista previa:
    - Partido: {}
    - Estadio: {}
    - Monto inicial: {}
    - Total Impuesto: {}
    - Total Descuento: {}
    - Monto final: {}
    """.format(partido_str, estadio_str, inicial, impuesto, descuento, total))

    while True:
        confirmacion = input("""
        1. Confirmar compra.
        2. Cancelar

        Ingrese el número de su eleccion: 
        """)
        if confirmacion != "1" and confirmacion != "2":
            print("Error")
        else:
            break

    if confirmacion == "1":
        print("\t\t\tCompra Exitosa!!!")
        consumo = []
        codigo = codigo_unico(codigo_compra)
        factura = {
            "codigo": codigo,
            "name": name,
            "id": id,
            "age": age,
            "partido": partido_escogido,
            "tipo": tipo,
            "asiento": asiento,
            "total": total,
            "consumo": consumo
        }
        lista_compras.append(factura)
        codigo_compra.append(codigo)
        imprimir_recibo(factura)
    else:
        print("\nCompra anulada.\n")

    return lista_compras

def codigo_unico(codigo_compra):
    while True:
        n = random.randint(1000, 9999)
        if n not in codigo_compra:
            break
    return n

def vampire(id):
    id_str = str(id)
    digitos = len(id_str)

    if digitos % 2 != 0 or digitos == 2:
        return False

    for x in range(1, (int(id) // 2 + 1)):
        for y in range(1, (int(id) // 2 + 1)):
            if str(x)[-1] == 0 and str(y)[-1] == 0:
                continue

            if len(str(x)) + len(str(y))!= digitos:
                continue

            if x * y == id:
                return True

    return False

def escoger_asiento(estadio, sector, partido_escogido):
    capacidad = estadio.get_capacity(estadio)

    capacidad_total = sum(capacidad)

    matriz_completa = crear_matriz(capacidad_total)

    numero_filas_vip = capacidad[1] // 10
    evip = []
    egen = []

    for i in range(0, numero_filas_vip):
        evip.append(matriz_completa[i])

    for i in range(numero_filas_vip, len(matriz_completa)):
        egen.append(matriz_completa[i])

    print("\n\n\n")

    if sector == "General":
        print("\t\tMatriz de Asientos General\n")
        print_e(egen)
        asiento = asiento_escogido(partido_escogido, estadio, egen)
    else:
        print("\t\tMatriz de Asientos VIP\n")
        print_e(evip)
        asiento = asiento_escogido(partido_escogido, estadio, evip)

    return asiento

def asiento_escogido(partido, estadio, selected_matrix):
    confirmation = False
    print("Asientos Ocupados: ")
    for asiento in partido.get_taken_seats(partido):
        print("- " + asiento)

    while True:
        try:
            asiento = input("Escriba el código del asiento que desea:").upper()

            for line in selected_matrix:
                if asiento in line:
                    confirmation = True
                    break

            if not confirmation:
                raise Exception

            if asiento in partido.get_taken_seats(partido):
                raise Exception

            break
        except:
            print("El asiento ingresado no es válido o se encuentra ocupado.")

    return asiento

def print_e(matrix):
    linea_str = ""

    for line in matrix:
        for seat in line:
            linea_str += seat
            linea_str += "  "

        print(linea_str)
        linea_str = ""

    print("")

def crear_matriz(capacidad):
    abecedario = list(string.ascii_uppercase)

    numero_filas = capacidad // 10

    filas_letras = []

    for i in range(0, numero_filas):
        filas_letras.append(abecedario[i])

    matrix = []

    for letra in filas_letras:
        linea = []
        for x in range(1, 11):
            linea.append(letra + str(x))
        matrix.append(linea)

    return matrix

def escoger_tipo_entrada():
    print("\n\nTipos de Entrada: \n1. General: 35$ \n\t- Solo podrá ver el partido desde su asiento. \n\n2. VIP: 75$ \n\t- Podrá disfrutar del restaurante del estadio.    ")

    while True:
        try:
            tipo_boleto = input("Ingrese el número de su selección:     ")

            if tipo_boleto!= "1" and tipo_boleto!= "2":
                raise Exception

            break
        except:
            print("Por favor, ingrese una opción válida.")

    if tipo_boleto == "1":
        tipo_boleto = "General"
    else:
        tipo_boleto = "VIP"

    return tipo_boleto

def escoger_partido(lista_partidos, lista_estadios):
    for partido in lista_partidos:
        partido.print_partido(partido)

    while True:
        try:
            id_partido = int(input("Ingrese el número del partido:"))

            if id_partido not in range(1, 49):
                raise Exception

            break
        except:
            print("Por favor, ingrese una opción válida.")

    for partido in lista_partidos:
        if partido.get_id(partido) == id_partido:
            return partido

def imprimir_recibo(factura):
    print("""
    Recibo de Compra:
    - Código: {}
    - Nombre: {}
    - Identificación: {}
    - Edad: {}
    - Partido: {}
    - Tipo: {}
    - Asiento: {}
    - Total: {}
    """.format(factura["codigo"], factura["name"], factura["id"], factura["age"], factura["partido"].get_name(), factura["tipo"], factura["asiento"], factura["total"]))                           