import requests

class Equipo(): 
    def __init__ (self, pais, codigo_FIFA, grupo, id):
        self.pais= pais 
        self.codigo_FIFA= codigo_FIFA
        self.grupo= grupo
        self.id= id

def show (self):
    print(self.pais, self.codigo_FIFA, self.grupo, self.id)

    def get_name(self): 
        return self.name

    def print_equipo(self): 
        print("""
            -----País: {}
            -----URL Flag: {}
            -----Código FIFA: {}
            -----Grupo: {}
            -----ID: {}
            """.format(self.name, self.flag, self.fifa_code, self.group, self.id))