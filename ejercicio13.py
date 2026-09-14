class CombinadorListas:

    def __init__(self):
        self.resultados = []

    def intercalar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = list(listas[0])

        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)

        return resultado


combinador = CombinadorListas()

print(combinador.intercalar([1, 2], [3, 4]))

print(combinador.intercalar_multiples([1, 2], [3, 4]))