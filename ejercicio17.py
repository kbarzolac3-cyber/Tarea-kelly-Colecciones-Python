class AgrupadorEdades:

    def __init__(self):
        self.edades = {
            "child": [],
            "teenager": [],
            "adult": [],
            "older adult": []
        }

    def clasificar_edad(self, edad):

        if edad < 13:
            return "child"

        elif edad < 18:
            return "teenager"

        elif edad < 60:
            return "adult"

        else:
            return "older adult"

    def agrupar_por_categoria(self, *edades):

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.edades[categoria].append(edad)

        return self.edades

    def edad_promedio_categoria(self, categoria):

        edades = self.edades[categoria]

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)


agrupador = AgrupadorEdades()

print(agrupador.agrupar_por_categoria(9, 16, 20, 30, 70))

print(agrupador.edad_promedio_categoria("adult"))