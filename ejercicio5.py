class AnalizadorNumeros:

    def __init__(self):
        self.numeros = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:
            self.numeros.append(numero)

            if self.es_par(numero):
                resultado["pares"].append(numero)
            else:
                resultado["impares"].append(numero)

        return resultado

    def cantidad_pares_impares(self):
        pares = 0
        impares = 0

        for numero in self.numeros:
            if self.es_par(numero):
                pares += 1
            else:
                impares += 1

        return (pares, impares)



analizador = AnalizadorNumeros()

print(analizador.separar(1, 2, 3, 4, 5))

print(analizador.cantidad_pares_impares())