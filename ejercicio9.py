class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        for letra in texto:

            if letra.isdigit():
                digitos += 1

            elif letra.isalpha():

                if self.solo_vocales(letra):
                    vocales += 1
                else:
                    consonantes += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }



analizador = AnalizadorString()

print(analizador.contar_por_tipo("Bienvenido123"))

print(analizador.texto_mas_largo)