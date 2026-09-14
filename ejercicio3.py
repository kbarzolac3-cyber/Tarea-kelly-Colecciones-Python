class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0

        for precio in self.articulos.values():
            total += precio

        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado



carro = CarroCompras()

carro.agregar_articulo("water", 1.50)
carro.agregar_articulo("milk", 2.00)
carro.agregar_articulo("lentil", 5.00)

print(carro.articulos)

print(carro.total_carrito())

print(carro.articulos_por_rango(2, 3))