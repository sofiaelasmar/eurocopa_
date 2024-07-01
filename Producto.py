class Producto():
    def __init__ (self, name, quantity, price, stock, tipo_producto):
        self.name= name
        self.quantity= quantity
        self.price= price
        self.stock= stock
        self.tipo_producto= tipo_producto


class Bebida (Producto):
    def __init__ (self, name, quantity, price, stock, tipo_producto, tipo_bebida):
        super().__init__(name, quantity, price, stock, tipo_producto)
        self.tipo_bebida= tipo_bebida


class Comida (Producto):
    def __init__ (self, name, quantity, price, stock, tipo_producto, adicional):
        super().__init__ (name, quantity, price, stock, tipo_producto)
        self.adicional= adicional

    def print_product_all(self):
        print("""
        Nombre:{}
        Cantidad: {}
        Precio: {}$
        Tipo: {}
        Adicional: {}
        """.format(self.name, self.quantity, self.price, self.type, self.adicional))

    def print_product_in_menu(self): 
        print("""
        Nombre:{}
        Precio: {}$
        Tipo: {}
        """.format(self.name, self.price, self.adicional))
    
    def get_price(self):
        return self.price

    def lower_quantity(self):
        self.quantity -= 1
    
    def get_quantity(self):
        return self.quantity

    def get_name(self):
        return self.name
