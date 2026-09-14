class AnalizadorTexto:

    def __init__(self):
        self.palabras = []
        self.unicas = set()

    def agregar_palabra(self, palabra):
        self.palabras.append(palabra)
        self.unicas.add(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)



analizador = AnalizadorTexto()

analizador.agregar_multiples("hello", "welcome", "hello")

print(analizador.palabras)
print(analizador.contar_palabras())