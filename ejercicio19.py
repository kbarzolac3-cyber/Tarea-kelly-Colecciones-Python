class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado



inventario = Inventario()

inventario.agregar_stock("sugar", 50)
inventario.agregar_stock("corn", 10)
inventario.agregar_stock("rice", 30)

print(inventario.stock)

print(inventario.restar_stock("sugar", 30))

print(inventario.stock)

print(inventario.productos_bajo_stock(25))