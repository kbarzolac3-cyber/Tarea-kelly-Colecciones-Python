class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = 0
        elemento_mayor = None

        for elemento, cantidad in self.frecuencias.items():
            if cantidad > mayor:
                mayor = cantidad
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0



contador = ContadorFrecuencia()

contador.agregar_elemento("e")
contador.agregar_elemento("b")
contador.agregar_elemento("e")
contador.agregar_elemento("c")
contador.agregar_elemento("e")

print(contador.frecuencias)

print(contador.elemento_mas_frecuente())

print(contador.frecuencia_elemento("e"))