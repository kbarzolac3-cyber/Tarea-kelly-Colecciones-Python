import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        cercano = puntos[0]
        distancia_menor = self.distancia_euclidiana(referencia, cercano)

        for punto in puntos[1:]:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                cercano = punto

        return cercano



calculador = CalculadorDistancia()

print(calculador.distancia_euclidiana((0, 0), (3, 4)))

print(calculador.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (5, 5)
))

print(calculador.distancias)