from Producto import Producto

class Estadio():
    def __init__ (self, id, name, city, capacity, restaurants, location):
        self.id= id
        self.name= name
        self.city= city
        self.capacity= capacity
        self.restaurants= restaurants        
        self.location= location 

    def show (self):
        print(self.id, self.name, self.city, self.capacity, self.restaurants)

    def print_Estadio(self): 
        print("""
        ID: {}
        Nombre: {}
        Capacidad: 
            VIP:{}   
            General:{}
        Locación: {}
        """.format(self.id, self.name, self.capacity[1], self.capacity[0], self.location))

    def print_Estadio_all(self):
        print("""
        ID: {}
        Nombre: {}
        Capacidad: 
            VIP:{}   
            General:{}
        Locación: {}
        """.format(self.id, self.name, self.capacity[1], self.capacity[0], self.location))
        self.print_restaurants()

    def get_Restaurante(self):
        return self.restaurants

    def print_Restaurante(self):
        for rest in self.restaurants: 
            print(rest["name"])
            print(" -Productos:")
            for p in rest["products"]:
                Producto.print_Producto_all(p)

    def get_capacidad(self):
        return self.capacity

    def get_name(self): 
        return self.name


