from Compra import main_compra
from Partido import Partido
from Estadio import Estadio
from Producto import Producto

class Restaurante():
    def __init__ (self, nombre, productos):
        self.nombre= nombre
        self.productos= productos

    def show (self):
        print(self.nombre, self.productos)

def start_restaurante(lista_compra):

    print("\nMÓDULO DE RESTAURANTES\n")

    print("Para ingresar en el módulo de restaurantes, debemos chequear si usted es un cliente VIP: \n\n")
    while True: 
        try: 
            id = int(input("\nIngrese su cédula:  "))

            if id <= 0: raise Exception
        
            break

        except: 
            print("ID inválido. ")
    

    #Comprobamos si el cliente es VIP.

    vip = False

    for f in lista_compra: 

        if id == main_compra.get_id(f):
            if "VIP" == main_compra.get_sector(f): 
                vip = True
                main_compra = f
            else: 
                print("Usted no compró VIP")
        else: 
            print("No aparece registrado en la base de datos.")
        

    if not vip:
        print("No puede pedir en restaurantes.")
        return 
    
    partido = main_compra.get_match(main_compra)
    estadio = partido.get_stadium(partido)
    restaurante = seleccionar_restaurante(estadio)
    
    #booleano que nos permite seguir llenando el carrito
    pedido = True
    carrito = []
    while pedido:
        orden = iniciar_orden(restaurante)
        if Producto.get_quantity(orden) == 0: 
            print("\nLamentablemente, nos hemos quedado sin ese producto.")
            continue
        carrito.append(orden)
        pedido = continuar_pedido()

    #Cuando ya no vamos a comprar más, procesamos el carrito. 
    total = procesar_carrito(carrito, id)

    if total == -1: 
        return 
    

    print("\n\nÉXITO EN PROCESAMIENTO DE COMPRA\n\n")
    print("\n-------------FACTURA-----------------\n")
    for p in carrito: 
        Producto.lower_quantity(p)
        Producto.print_product_in_menu(p)
        print("-------------------------")
    print("------------------------Monto Final: {}$".format(total))
    print("///////////////////////////////////")

    main_compra.set_consumo(main_compra, carrito)
    main_compra.sumar_comsumo(main_compra, total)




def procesar_carrito(carrito, id):
    """Efectuamos la transacción de pago. 
    """    
    print("\n\nResumen del carrito: ")
    
    monto = 0
    for p in carrito: 
        print("")
        Producto.print_product_in_menu(p)
        monto += Producto.get_price(p)
    
    iva = monto*0.16

    discount = 0
    if perfecto(id):
        discount = monto*0.15
        print("\t\t\tSu cedula es un numero perfecto, usted obtiene un '15%' de descuento!!!.")

    total = monto + iva 
    total -= discount

    print("""
    ////////////////////////////////////////////
    \t\t\t\Resumen de Costos 
    ***Monto Inicial:{}
    ***Impuesto (IVA del 16%):{}
    ***Descuento:{}
    ***Monto Final:{}
    """.format(monto, iva, discount, total))

    while True: 
        confirmacion_de_compra = input("""\n\n---¿Desea realizar su compra? 
            1. sí 
            2. no
            """)
        
        if confirmacion_de_compra == "1" or confirmacion_de_compra == "no": 
            break 

        print("\nEl valor ingresado no es válido.")

    if confirmacion_de_compra == "1": 
        return total
    else:
        return -1


def perfecto(n): 
    divs = 1
    n = int(n)
    for x in range(2, (n//2)+1):
        if n%x==0: 
            divs += x
    
    if divs == n:
        return True
    return False


def continuar_pedido(): 
   
    while True: 
        fin = input("""
                \nIndique si finalizó de pedir. 
                En caso de que sí, se procesa la compra. Si desea comprar otro producto, responda NO.
                Escriba "1" para SÍ y "2" para NO:\n  
                """)
        
        if fin == "1" or fin == "2":
            break
        else: print("\n Respuesta Inválida.")

    if fin == "1": 
        return False
    else: 
        return True

def iniciar_orden(restaurante):
   
    print("")
    
    print("Menú del {}".format(restaurante["name"]))

    #Formato de Restaurante: {'name': '974 Restaurant', 'products': [<product.Product object at 0x7fc3774a8c88>, <product.Product object at 0x7fc3774a8cc0>, <product.Product object at 0x7fc3774a8cf8>, <product.Product object at 0x7fc3774a8d30>]}

    x = 0
    for p in restaurante["products"]:
        x += 1
        print("--------------------\n\t{}".format(x))
        Producto.print_product_all(p)
        print("--------------------")

    while True: 
        try:
            seleccion = int(input("Ingrese el número de la comida a adquirir:   "))

            if seleccion not in range (1, len(restaurante["products"]) + 1):
                raise Exception

            break

        except: 
            print("Ingrese una opción válida.")

    seleccion -= 1 

    p_seleccionado_objeto = restaurante["products"][seleccion]

    return p_seleccionado_objeto



def seleccionar_restaurante(estadio): 
   
    rests_list = estadio.get_restaurants(estadio)

    estadio_name = estadio.get_name(estadio)

    i = 0

    print("\n\nLos restaurantes disponibles en el {} son: ".format(estadio_name))
    for rest in rests_list: 
        i += 1
        print("\n\t\t")
        print(str(i) + "- " + rest["name"])
    
    print("")

    while True: 
        try: 
            escogido = int(input("\nIngrese la selección de su restaurante: "))

            if len(rests_list) == 1 and escogido != 1: 
                raise Exception

            if escogido not in range(1, len(rests_list)+1):    raise Exception

            break

        except: 

            print("Valor no adecuado a la pregunta.")

    index = escogido - 1
    seleccionado = rests_list[index] 
    
    #Diccionario del restaurante. 
    
    return seleccionado