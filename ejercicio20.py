class AnalizadorPatrones:

    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        resultado = []

        for palabra in texto.split():
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}

        for palabra in texto.split():
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self):
        return set(self.palabras)



analizador = AnalizadorPatrones()

texto = "hello world hello python"

print(analizador.encontrar_palabras(texto, "he"))

print(analizador.agrupar_por_longitud(texto))

analizador.palabras = texto.split()

print(analizador.palabras_unicas())