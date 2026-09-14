class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return



tareas = Tareas()

tareas.agregar_tarea("Practice Python", "alta")
tareas.agregar_tarea("Do English homework", "media")
tareas.agregar_tarea("Go for a run", "alta")

print(tareas.tareas)

print(tareas.tareas_prioritarias())

tareas.eliminar_completada("Go for a run")

print(tareas.tareas)