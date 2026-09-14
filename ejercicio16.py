class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        inicio = ord('a')
        posicion = ord(letra.lower()) - inicio
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(inicio + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()

print(codificador.codificar_letra("a", 3))

print(codificador.codificar_palabra("hola", 3))

print(codificador.historial)