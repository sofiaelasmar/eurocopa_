import requests
from Comprar_Entradas import main_compra
from Compra import main_compra
from Partido import Partido
import Autenticar
from Estadisticas import Estadisticas
from Restaurante import Restaurante
import json 

def main(): 

    lista_equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
    lista_estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()
    lista_partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()

    lista_compra = [] 
    #Listas de objeto compra

    
    compra_id = [] #codigos de factura dados, para que cada factura tenga su propio codigo 
    boletos_validados = [] #Guarda los id que ya han sido validados para lanzar error cuando se presente un id que ya fue registrado 

    print("\t\t\t PROYECTO EUROCOPA")

    while True: 
       
        print("""
        Menú: 
        1.- Comprar boleto
        2.- Autentificación de Boletos
        3.- Restaurantes
        4.- Estadísticas 
        5.- Imprimir boletos
        6.- Salir
        """)

        while True:
            try: 
                accion = int(input("\nIngrese el número de lo que desea realizar:"))

                if accion not in range(1, 7):
                    raise Exception

                break

            except: 
                print("\nError. Escriba una opción válida..\n")

        
        if accion == 1: 

            Compra(lista_estadios, lista_partidos, lista_compra, compra_id)

            pass

        elif accion == 2: 

            #pedimos el código para proceder a autenticarlo. 
            recibo_id = Autenticar.id_factura()

            #Recibimos el True si es válido.
            validado = Autenticar.validacion(lista_compra, recibo_id, boletos_validados)

            if validado: 

                print("\n\tAutentificación completada con éxito!\n")
                for p in lista_compra:
                    if recibo_id == Compra.get_code(p):
                        recibo = p

                partido = Compra.get_partido(recibo)

                boletos_validados.append(recibo_id)

                #subir el valor a los asistentes. 
                Partido.new_asistente(partido) 
            
            else: 
                print("\n\n Su boleto es falso. Ingrese un ID válido.\n\n")

            pass
        
        elif accion == 3:
            Restaurante(lista_compra)
  
        elif accion == 4: 
            Estadisticas(lista_partidos, lista_compra)

        elif accion == 5: 
            guardar = ""
            for Compra in lista_compra:
                str_compra = main_compra.get_string_all(main_compra)
                guardar += str_compra + "\n"
                print("------------------------") 
                main_compra.print_receipt(main_compra)
                print("------------------------") 

          
            with open("COMPRAS.txt", "w") as a:
                    a.write("CLIENTES:\n")
                    a.write(guardar)
                    a.write("")
            break

        else: 
            print("\nCERRANDO")
            break
            

    
main()
