from Estadio import Estadio
from Equipo import Equipo

class Competencia:
    def __init__(self, partidos, estadios):
        self.partidos = partidos       
        self.estadios = estadios

    def buscar_pais(self): 

        while True: 
            try: 
                pais = str(input("\n\nNombre del País:"))

                if not "".join(pais.split()).isalpha():
                    raise Exception 

                break 

            except: 
                print("\nError. Vuelva a intentar.\n")

        pais = pais.title()

        found = []

        for partido in self.partidos:

            if pais in partido.get_pais(partido): 
                found.append(partido)

        self.print_found(found)


    def buscar_estadio(self): 
        for estadio in self.estadios: 
            Estadio.print_stadium(estadio)

        while True: 
            try: 
                selection = int(input("ID del estadio: "))

                if selection not in range(1, 9): 
                    raise Exception

                break 

            except: 
                print("\nError. ID de estadio inválido.\n")


        selected_obj = self.estadios[selection-1]

        found = []

        for partidos in self.partidos:
            if selected_obj == partidos.get_estadio(partidos):
                found.append(partidos)

        self.print_found(found)


    def buscar_fecha(self): 
        print("\nBuscando por fecha:\n")

        while True: 
            try: 
                day = input("Día a buscar: ")
                month = input("Mes a buscar (número): ")
           
                if int(day) in range(1,32) and int(month) in range(1,13):
                    break

            except: 
                print("\n La información específicada no es correcta. \n")


        date = month + "/" + day + "/2024"

        found = []
        for partido in self.partidos: 
            if date in partido.get_date(partido):
                found.append(partido)

        self.print_found(found)
        

    def print_found(self, found): 
        print("RESULTADOS DE BÚSQUEDA")
        for part in found: 
            part.print_partido(part)