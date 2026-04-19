class Auto:
    def __init__(self, marca, color, ruedas, modelo):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        self.modelo = modelo

# Probar lo que hicimos
mi_auto1 = Auto("Mazda", "Blanco", 3, 2000)
def mostrar_auto1(auto1):
    print("===== Auto 1 =====")
    print(f"marca: {mi_auto1.marca}")
    print(f"color: {mi_auto1.color}")
    print(f"ruedas: {mi_auto1.ruedas}")
    print(f"modelo: {mi_auto1.modelo}")
    print("=================\n")

mostrar_auto1(mi_auto1)

mi_auto2 = Auto("Chevrolet", "Azul", 4, 1995)
def mostrar_auto2(auto2):
    print("===== Auto 2 =====")
    print(f"marca: {mi_auto2.marca}")
    print(f"color: {mi_auto2.color}")
    print(f"ruedas: {mi_auto2.ruedas}")
    print(f"modelo: {mi_auto2.modelo}")
    print("=================\n")

mostrar_auto2(mi_auto2)


mi_auto3 = Auto("Ferrary", "Rojo", 3, 1999)
def mostrar_auto3(auto3):
    print("===== Auto 3 =====")
    print(f"marca: {mi_auto3.marca}")
    print(f"color: {mi_auto3.color}")
    print(f"ruedas: {mi_auto3.ruedas}")
    print(f"modelo: {mi_auto3.modelo}")
    print("=================\n")

mostrar_auto3(mi_auto3)

class Vuelo:
    def __init__(self, numeroVuelo, origen, destino, capacidadPasajeros):
        self.numeroVuelo = numeroVuelo
        self.origen = origen
        self.destino = destino
        self.capacidadPasajeros = capacidadPasajeros

mi_vuelo1 = Vuelo("A588", "Bogota", "Madrid", "300")
def mostrar_vuelo1(vuelo1):
    print("==== Vuelo 1 ====")
    print(f"numeroVuelo: {mi_vuelo1.numeroVuelo}")
    print(f"origen: {mi_vuelo1.origen}")
    print(f"destino: {mi_vuelo1.destino}")
    print(f"capacidadPasajeros: {mi_vuelo1.capacidadPasajeros}")
    print("=================\n")

mostrar_vuelo1(mi_vuelo1)

mi_vuelo2 = Vuelo("A333", "Madrid", "Buenos Aires", "150")
def mostrar_vuelo2(vuelo2):
    print("==== Vuelo 2 ====")
    print(f"numeroVuelo: {mi_vuelo2.numeroVuelo}")
    print(f"origen: {mi_vuelo2.origen}")
    print(f"destino: {mi_vuelo2.destino}")
    print(f"capacidadPasajeros: {mi_vuelo2.capacidadPasajeros}")
    print("=================\n")

mostrar_vuelo2(mi_vuelo2)

mi_vuelo3 = Vuelo("LA800", "Cartagena", "Bogota", "100")
def mostrar_vuelo3(vuelo3):
    print("==== Vuelo 3 ====")
    print(f"numeroVuelo: {mi_vuelo3.numeroVuelo}")
    print(f"origen: {mi_vuelo3.origen}")
    print(f"destino: {mi_vuelo1.destino}")
    print(f"capacidadPasajeros: {mi_vuelo3.capacidadPasajeros}")
    print("=================\n")

mostrar_vuelo3(mi_vuelo3)

class Horario:
    def __init__(self, jornada, numeroSalon, semestre, asignatura):
        self.jornada = jornada
        self.numeroSalon = numeroSalon
        self.semestre = semestre 
        self.asignatura = asignatura


mi_horario1 = Horario("Noche", "11", "1", "Igles 1")
def mostrar_horario1(Horario1):
    print("==== Horario 1 ====")
    print(f"jornada: {mi_horario1.jornada}")
    print(f"numeroSalon: {mi_horario1.numeroSalon}")
    print(f"semestre: {mi_horario1.semestre}")
    print(f"asignatura: {mi_horario1.asignatura}")
    print("=================\n")

mostrar_horario1(mi_horario1)

mi_horario2 = Horario("Noche", "7", "2", "Progracion I")
def mostrar_horario2(Horario2):
    print("==== Horario 2 ====")
    print(f"jornada: {mi_horario2.jornada}")
    print(f"numeroSalon: {mi_horario2.numeroSalon}")
    print(f"semestre: {mi_horario2.semestre}")
    print(f"asignatura: {mi_horario2.asignatura}")
    print("=================\n")

mostrar_horario2(mi_horario2)

mi_horario3 = Horario("Fin de semana", "17", "2", "Calculo diferencial")
def mostrar_horario3(Horario3):
    print("==== Horario 3 ====")
    print(f"jornada: {mi_horario3.jornada}")
    print(f"numeroSalon: {mi_horario3.numeroSalon}")
    print(f"semestre: {mi_horario3.semestre}")
    print(f"asignatura: {mi_horario3.asignatura}")
    print("=================\n")

mostrar_horario3(mi_horario3)