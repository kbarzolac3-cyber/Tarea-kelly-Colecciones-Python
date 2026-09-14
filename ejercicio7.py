class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)



gestor = GestorPersonas()

gestor.agregar_persona("Jose", 29)
gestor.agregar_persona("Kelly", 18)
gestor.agregar_persona("Elian", 22)

print(gestor.personas)
print(gestor.personas_mayores(18))
print(gestor.edad_promedio())