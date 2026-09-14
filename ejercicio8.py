class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = ""
        cantidad_mayor = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad_mayor:
                cantidad_mayor = len(jugadores)
                mayor = equipo

        return mayor



equipos = Equipos()

equipos.crear_equipo("Barcelona")
equipos.crear_equipo("Emelec")

equipos.agregar_jugador("Barcelona", "Luis")
equipos.agregar_jugador("Barcelona", "Matias")
equipos.agregar_jugador("Barcelona", "David")

equipos.agregar_jugador("Emelec", "Carlos")
equipos.agregar_jugador("Emelec", "Josue")

print(equipos.equipos)
print(equipos.equipo_mayor_integrantes())