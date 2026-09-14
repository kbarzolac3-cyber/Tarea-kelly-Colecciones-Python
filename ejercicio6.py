class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)



gt = GestorTemperatura()

gt.registrar_multiples(15, 35, 27, 20)

print(gt.temperaturas)
print(gt.minima())
print(gt.maxima())
print(gt.promedio())

  
 





