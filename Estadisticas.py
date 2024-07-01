from Compra import main_compra
from Partido import Partido
from Producto import Comida 

def Estadisticas(lista_partidos, lista_compras):
    
    print("""\n
                    ESTADÍSTICAS 

    Opciones Disponibles
    1.- Promedio de gasto de un cliente VIP en un partido (ticket + restaurante):
    2.- Tabla de asistencia a los partidos:       
    3.- Partido con mayor asistencia:
    4.- Partido con mayor numero dee boletos vendidos:
    5.- Top 3 productos mas vendidos en el restaurante:
    6.- Top 3 clientes (con mayor numero de boletos comprados):
    """)

    while True:
        
        try: 
            stat = int(input("\n\n\tEstadística a ver:    "))
            if stat in range(1, 7):
                break
            else:
                raise Exception

        except: 
            print("Ingrese un valor válido.")

    #Distribuimos el programa. 
    if stat == 1:  promedio_gvip(lista_compras)
    elif stat == 2:  tabla(lista_partidos)
    elif stat == 3:  mayor_asistencia(lista_partidos)
    elif stat == 4:  mayor_venta(lista_partidos)
    elif stat == 5:  productos_mas_vendidos(lista_compras)
    elif stat == 6:  top_clientes(lista_compras) 
    else: print("lol")


def promedio_gvip(lista_purchases):
    cliente_vip = 0
    cantidad = 0
    for a in lista_purchases: 
        if main_compra.get_sector(a) == "VIP":
            cliente_vip += 1
            cantidad += float(main_compra.get_monto(a))
            
    if cliente_vip == 0: 
        print("Aún no hay clientes VIP registrados.")
        return

    promedio = cantidad/cliente_vip

    print("El promedio de un cliente VIP es:    " + str(promedio) + "\n\n")

def tabla(lista_partidos): 
    """Agarramos la lista de asistencia ordenada y formamos una tabla yendo secuencialmente preguntando qué asistencia tiene cada juego. 

    """    
    asistencia = ordenar_asist(lista_partidos)

    print("\n\n Tabla de Asistencia: ")
    for n in asistencia:
        print("Asistencia de " + str(n))
        for partido in lista_partidos: 
            if partido.get_asistentes(partido)==n:
                print("     -" +partido.get_info(partido))


def mayor_asistencia(lista_partidos):
       

    print("Entré")
    asistencia_ordenada = ordenar_asist(lista_partidos)

    for match in lista_partidos: 
        if asistencia_ordenada[0]== Partido.get_asistentes(match):
            found = match


    print("\n\n\tEl partido con mayor asistencia fue {} con una asistencia de {} personas.".format(Partido.get_info(found), asistencia_ordenada[0]))

def mayor_venta(lista_partidos):

    ventas_ordenadas = ordenar_por_ventas(lista_partidos)

    for partido in lista_partidos: 
        if ventas_ordenadas[0]== partido.get_vendido(partido):
            found = partido
            


    print("\n\n\tEl partido con mayores ventas fue {} con un de {} boletos vendidos.".format(partido.get_info(found), ventas_ordenadas[0]))


def productos_mas_vendidos(lista_purchases):


    vendidos = {}

    for x in lista_purchases:
        consumo = main_compra.get_consumo(x)
        if len(consumo) == 0: continue
        for product in consumo: 
            if product in vendidos: 
                vendidos[product] = vendidos[product]+1
            else: 
                vendidos[product] = 1

    sorted_vendidos = sorted(vendidos.items(), key=lambda x:x[1]) #De menor a mayor, lista de tuplas. 
    
    if len(sorted_vendidos) == 0:
        print("Aún no se ha vendido nada.")
        return

    #Ordenamos diccionario.
    if len(sorted_vendidos) >= 3: 
        for i in range(1, 4):
            top_vendidos_tuplas = [sorted_vendidos[-i]]
    else: 
        for i in range(1, len(sorted_vendidos)+1):
            top_vendidos_tuplas = [sorted_vendidos[-i]]

    top_vendidos_dict =  dict(top_vendidos_tuplas)

    for key, value in top_vendidos_dict.items(): 
        print("Los productos más vendidos son: ")
        print(productos_mas_vendidos.get_name(key) + " vendido " + str(value) + " veces.")

def top_clientes(lista_purchases): 
    clientes_id = {} #ID y cantidad de veces que sale.
    
    for purchase in lista_purchases: 
        id = main_compra.get_id(purchase)
        if id in clientes_id: 
            clientes_id[id] += 1
        else: 
            clientes_id[id] = 1

    #Ordenamos diccionario.
    ordenar_clientes = sorted(clientes_id.items(), key=lambda x:x[1]) #De menor a mayor, lista de tuplas. 
    
    if len(ordenar_clientes) == 0:
        print("Aún no se ha vendido nada.")
        return

    if len(ordenar_clientes) >= 3: 
        for i in range(1, 4):
            top_clientes = [ordenar_clientes[-i]]

    else: 
        for i in range(1, len(ordenar_clientes+1)):
            top_clientes = [ordenar_clientes[-i]]

    top_clients_dict =  dict(top_clientes)

    for key, value in top_clients_dict.items(): 
        print("Los clientes con más boletos son: ")
        print("El cliente ID: " + str(key) + " con un total de " + str(value) + " boletos.")



def ordenar_por_ventas(lista_partidos):
    """Tomo todas las ventas, borro las repetidas y devuelvo las listas ordenadas. 
    """
    all_ventas = []
    for p in lista_partidos: 
        all_ventas.append(Partido.get_vendido(p))

    vendidos_n = list(set(all_ventas))

    vendidos_ordenados = sorted(vendidos_n, reverse=True)

    return vendidos_ordenados

def ordenar_asist(lista_partidos):
    """Primero, tenemos todas la asistencias a todos los partidos, luego, eliminamos los valores repetidos y ordenamos la lista.
    """
    
    all_asistencias = []
    for p in lista_partidos: 
        all_asistencias.append(Partido.get_asistentes(p))

    asistencias_valores = list(set(all_asistencias))

    asistentes_ordenados = sorted(asistencias_valores, reverse=True)

    return asistentes_ordenados