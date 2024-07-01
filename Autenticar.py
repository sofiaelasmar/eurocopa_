from Compra import main_compra

def id_factura():
    while True:
        try:
            factura_id = int(input("\n\nIngrese el código único de su factura:   "))
            if factura_id <= 0:
                print("El ID de la factura debe ser un número positivo")
                continue
            return factura_id
        except ValueError:
            print("Ingrese un ID válido")

def validacion(lista_compras, factura_id, boletos_validados):
    if not lista_compras or not boletos_validados:
        raise ValueError("Lista de compras y boletos validados no pueden ser vacíos")
    if not isinstance(factura_id, int):
        raise ValueError("El ID de la factura debe ser un número entero")
    codes = [main_compra.get_code(p) for p in lista_compras]
    if factura_id not in codes:
        print("El ID de la factura no es válido")
        return False
    return factura_id not in boletos_validados