from Partido import Partido
from Estadio import Estadio

class main_compra:
    def __init__(self, code, name, id, edad, partido, sector, asiento, cantidad, consumo=None):
        self.code = code
        self.name = name
        self.id = id
        self.edad = edad
        self.partido = partido
        self.sector = sector
        self.asiento = asiento
        self.cantidad = cantidad
        self.consumo = consumo if consumo is not None else []

    def print_recibo(self):
        partido_str = Partido.get_info(self.partido)
        print("""
        -------------------------------------------
        \t\t\t FACTURA #{}
        Nombre: {}
        ID: {}
        Edad: {}
        Partido: {}
        Tipo de entrada: {}
        Asiento: {}
        Monto: {}
        --------------------------------------------
        """.format(self.code, self.name, self.id, self.edad, partido_str, self.sector, self.asiento, self.cantidad))

    def get_code(self):
        return self.code

    def get_partido(self):
        return self.partido

    def get_id(self):
        return self.id

    def get_sector(self):
        return self.sector

    def get_monto(self):
        return self.cantidad

    def get_consumo(self):
        return self.consumo

    def set_consumo(self, carrito):
        self.consumo = carrito

    def sumar_consumo(self, monto):
        self.cantidad += monto

    def get_string_all(self):
        partido_info = Partido.get_info(self.partido)
        string = """
            -------------------------------------------
            \t\t\t Compra #{}
            Nombre: {}
            ID: {}
            Edad: {}
            Partido: {}
            Tipo de entrada: {}
            Asiento: {}
            Monto: {}
            Consumo: {}
        --------------------------------------------
        """.format(self.code, self.name, self.id, self.edad, partido_info, self.sector, self.asiento, self.cantidad, self.consumo)
        return string
