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

# Clase Vuelo: ejercicio 1

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

# Clase Horario: ejercicio 2

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

# Clase Ttelevisor: ejercicio 3

class Televisor:
    def __init__(self, marca, tamaño, smartTV, tieneTDT):
        self.marca = marca
        self.tamaño = tamaño
        self.smartTV = smartTV
        self.tieneTDT = tieneTDT

mi_televisor1 = Televisor("LG", "50", "True", "True")
def mostrar_televisor1(televisor1):
    print("==== televisor 1 ====")
    print(f"marca: {mi_televisor1.marca}")
    print(f"tamaño: {mi_televisor1.tamaño}")
    print(f"smartTV: {mi_televisor1.smartTV}")
    print(f"tieneTDT: {mi_televisor1.tieneTDT}")
    print("=================\n")

mostrar_televisor1(mi_televisor1)

mi_televisor2 = Televisor("TLC", "77", "True", "True")
def mostrar_televisor2(televisor2):
    print("==== televisor 2 ====")
    print(f"marca: {mi_televisor2.marca}")
    print(f"tamaño: {mi_televisor2.tamaño}")
    print(f"smartTV: {mi_televisor2.smartTV}")
    print(f"tieneTDT: {mi_televisor2.tieneTDT}")
    print("=================\n")

mostrar_televisor2(mi_televisor2)

mi_televisor3 = Televisor("Panasonic", "22", "False", "False")
def mostrar_televisor3(televisor3):
    print("==== televisor 3 ====")
    print(f"marca: {mi_televisor3.marca}")
    print(f"tamaño: {mi_televisor3.tamaño}")
    print(f"smartTV: {mi_televisor3.smartTV}")
    print(f"tieneTDT: {mi_televisor3.tieneTDT}")
    print("=================\n")

mostrar_televisor3(mi_televisor3)

# Clase Cuaderno: ejercicio 4 

class Cuaderno:
    def __init__(self, tamaño, cantidadHojas, tipoHoja, tipoGama):
        self.tamaño = tamaño
        self.cantidadHojas = cantidadHojas
        self.tipoHoja = tipoHoja
        self.tipoGama = tipoGama

mi_cuaderno1 = Cuaderno("Grande", "100", "Rayado", "Bajo")
def mostrar_cuaderno1(cuaderno1):
    print("==== Cuaderno 1 ====")
    print(f"tamaño: {mi_cuaderno1.tamaño}")
    print(f"cantidadHoja: {mi_cuaderno1.cantidadHojas}")
    print(f"tipoHoja: {mi_cuaderno1.tipoHoja}")
    print(f"tipoGama: {mi_cuaderno1.tipoGama}")
    print("=================\n")

mostrar_cuaderno1(mi_cuaderno1)

mi_cuaderno2 = Cuaderno("Pequeño", "50", "Cuadriculado", "Alta")
def mostrar_cuaderno2(cuaderno2):
    print("==== Cuaderno 2 ====")
    print(f"tamaño: {mi_cuaderno2.tamaño}")
    print(f"cantidadHoja: {mi_cuaderno2.cantidadHojas}")
    print(f"tipoHoja: {mi_cuaderno2.tipoHoja}")
    print(f"tipoGama: {mi_cuaderno2.tipoGama}")
    print("=================\n")

mostrar_cuaderno2(mi_cuaderno2)

mi_cuaderno3 = Cuaderno("Mediano", "100", "Ferrocarril", "Media")
def mostrar_cuaderno3(cuaderno3):
    print("==== Cuaderno 3 ====")
    print(f"tamaño: {mi_cuaderno3.tamaño}")
    print(f"cantidadHoja: {mi_cuaderno3.cantidadHojas}")
    print(f"tipoHoja: {mi_cuaderno3.tipoHoja}")
    print(f"tipoGama: {mi_cuaderno3.tipoGama}")
    print("=================\n")

mostrar_cuaderno3(mi_cuaderno3)

# Clase Videojuego: ejercicio 5 


class Videojuego:
    def __init__(self, titulo, plataforma, multijugador, tipoJuego):
        self.titulo = titulo
        self.plataforma = plataforma
        self.multijugador = multijugador
        self.tipoJuego = tipoJuego

mi_videojuego1 = Videojuego("Call of Duti", "Consola", "No", "Accion")
def mostrar_videojuego1(videojuego1):
    print("=== Videojuego 1 ===")
    print(f"titulo: {mi_videojuego1.titulo}")
    print(f"plataforma: {mi_videojuego1.plataforma}")
    print(f"multijugador: {mi_videojuego1.multijugador}")
    print(f"tipoJuego: {mi_videojuego1.tipoJuego}")
    print("=================\n")

mostrar_videojuego1(mi_videojuego1)

mi_videojuego2 = Videojuego("Super Mario", "PC", "No", "Accion")
def mostrar_videojuego2(videojuego2):
    print("=== Videojuego 2 ===")
    print(f"titulo: {mi_videojuego2.titulo}")
    print(f"plataforma: {mi_videojuego2.plataforma}")
    print(f"multijugador: {mi_videojuego2.multijugador}")
    print(f"tipoJuego: {mi_videojuego2.tipoJuego}")
    print("=================\n")

mostrar_videojuego2(mi_videojuego2)

mi_videojuego3 = Videojuego("Shadow Gambit", "PS5", "Si", "Estrategia")
def mostrar_videojuego3(videojuego3):
    print("=== Videojuego 3 ===")
    print(f"titulo: {mi_videojuego3.titulo}")
    print(f"plataforma: {mi_videojuego3.plataforma}")
    print(f"multijugador: {mi_videojuego3.multijugador}")
    print(f"tipoJuego: {mi_videojuego3.tipoJuego}")
    print("=================\n")

mostrar_videojuego3(mi_videojuego3)



