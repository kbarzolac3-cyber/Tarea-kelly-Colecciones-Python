class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)



calificador = Calificador()

print(calificador.cargar_notas(72, 95, 110, 84, -5, 70))

print(calificador.promedio()) 

 
