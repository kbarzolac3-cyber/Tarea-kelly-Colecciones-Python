class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor = None
        nota_mayor = 0

        for estudiante, nota in self.notas.items():
            if nota > nota_mayor:
                nota_mayor = nota
                mejor = estudiante

        return (mejor, nota_mayor)



registro = RegistroNotas()

registro.registrar("Mixi", 97)
registro.registrar("Vicente", 75)
registro.registrar("Leo", 80)

print(registro.notas)

print(registro.estudiantes_aprobados(70))

print(registro.mejor_estudiante())