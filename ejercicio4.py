class InversorSecuencia:

    def __init__(self):
        self.resultados = []

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)

        return resultado



inversor = InversorSecuencia()

lista = [1, 2, 3, 4, 5]

print(inversor.invertir_lista(lista))

print(inversor.invertir_multiples([1, 2, 3], [4, 5, 6]))