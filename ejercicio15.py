class DivisorFinder:

    def __init__(self):
        self.divisores = {}

    def encontrar_divisores(self, numero):
        resultado = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                resultado.append(i)

        return tuple(resultado)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado



finder = DivisorFinder()

print(finder.encontrar_divisores(12))

print(finder.es_perfecto(6))

print(finder.encontrar_multiples_divisores(6, 12))