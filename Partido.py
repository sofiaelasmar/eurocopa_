from Estadio import Estadio
from Equipo import Equipo

class Partido ():
    def __init__ (self, id, number, home, code, name, group, stadium_id, fecha_hora):
        self.id= id 
        self.number= number
        self.home= home
        self.code= code
        self.name= name
        self.group= group
        self.stadium_id= stadium_id
        self.fecha_hora= fecha_hora

    def show (self):
        print (self.id, self.number, self.home, self.code, self.name, self.group, self.stadium_id, self.fecha_hora
)
        
    def print_partido(self): 
              
        estadio_str = Estadio.get_name(self.estadio)
        local_str = Equipo.get_name(self.local)
        visitante_str = Equipo.get_name(self.visitante)

        print("""
        Partido #{}
        Local: {}
        Visitante: {}
        Fecha y Hora: {}
        Estadio: {}
        """.format(self.id_partido, local_str, visitante_str, self.date, estadio_str)) 

    def get_countries(self): 
       
        countries = ""

        local_str = Equipo.get_name(self.local)
        visitante_str = Equipo.get_name(self.visitante)

        countries = local_str + " vs. " + visitante_str

        return countries

    def get_stadium(self): 
        return self.estadio

    def get_date(self): 
        return self.date

    def get_id(self): 
        return self.id_partido

    def get_taken_seats(self): 
        return self.taken_seats

    def get_info(self): 
        local_str = Equipo.get_name(self.local)
        visitante_str = Equipo.get_name(self.visitante)


        ##2-   England vs. Iran // 11/21/2022 16:00
        info = "#" + str(self.id_partido) + "-   " + local_str + " vs. " + visitante_str + " // " + str(self.date)
        return info

    def get_asistentes(self):
        return self.asistentes

    def get_vendido(self):
        return self.vendidos

    def new_venta(self): 
        self.vendidos += 1

    def new_asistente(self):
        self.asistentes += 1

    def new_taken_seat(self, seat): 
        self.taken_seats.append(seat)