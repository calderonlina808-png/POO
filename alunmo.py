class Alumno:

        def __init__(self, nombre: str, edad: int, matricula: str):
            self.nombre = nombre
            self.edad = edad
            self.matricula = matricula
        def describir(self) -> str:
            return f"Hola, soy {self.nombre}, tengo {self.edad}, años y mi numero de matricula es {self.matricula} "
        def validar_edad(self) -> str:
            if self.edad < 18:
                return "Soy menor de edad"
            elif self.edad < 25:
                return "Soy joven"
            elif self.edad < 50:
                return "Soy adulto"
            else:
                return "Adulto mayor"

# Bloque de prueba ejercicio en clase (se ejecuta solo al correr el archivo directamente)

if __name__ == "__main__":
    Hector = Alumno("Hector Benavides", 58, "79756893")
    print("                                              CLASE ALUMNO                                             ")
    print(" ")
    print(" --------------------------------------------    Alumno1   --------------------------------------------")
    print(Hector.describir(), Hector.validar_edad())
    print(" ")

alumno1 = Alumno("Sofia Hernandez", 33, "34576859" )
print(" --------------------------------------------    Alumno2   --------------------------------------------")
print(alumno1.describir(), alumno1.validar_edad())
print(" ")

alumno2 = Alumno("Carol Sanchez", 17, "54768594" )
print(" --------------------------------------------    Alumno3   --------------------------------------------")
print(alumno2.describir(), alumno2.validar_edad())
print(" ")

# Clase Vuelo: ejercicio a desarrollar en clase (Indivudual)

class Vuelo:
    def __init__(self, numeroVuelo, origen, destino, capacidadPasajeros):
        self.numeroVuelo = numeroVuelo
        self.origen = origen
        self.destino = destino
        self.capacidadPasajeros = capacidadPasajeros
    def describir1(self) -> str:
            return f"Detalle del Vuelo, origen: {self.origen}, - Destino; {self.destino}, con numero de vuelo {self.numeroVuelo} y capacidad de pasajeros {self.capacidadPasajeros}. Viaja en un: "
    def validar_capacidadPasajeros(self) -> str:
            if self.capacidadPasajeros < 150:
                return "Avión pequeño"
            elif self.capacidadPasajeros < 300:
                return "Avión mediano"
            else:
                return "Avión grande"

if __name__ == "__main__":
    vuelo1 = Vuelo("A5054", "Bogota", "Cartagena",  150)
print("                                              CLASE VUELO                                             ")
print(" ")
print(" --------------------------------------------    Vuelo1   --------------------------------------------")
print(vuelo1.describir1(), vuelo1.validar_capacidadPasajeros())
print(" ")

vuelo2 = Vuelo("E5946", "Bogota", "Madrid", 500 )
print(" --------------------------------------------    Vuelo2   --------------------------------------------")
print(vuelo2.describir1(), vuelo2.validar_capacidadPasajeros())
print(" ")

vuelo3 = Vuelo("J8454", "londres", "Estambul", 700 )
print(" --------------------------------------------    Vuelo3   --------------------------------------------")
print(vuelo3.describir1(), vuelo3.validar_capacidadPasajeros())
print(" ")


# Clase Vuelo: ejercicio grupal en clase.

class Vuelo:
    def __init__(self, origen, destino, fecha, hora, precio, tipoV, activo):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.precio = precio
        self.tipoV = tipoV
        self.activo = activo

    def clasificacion_tipoVuelo(self) ->str:
        if self.tipoV == 1:
            return "Vuelo Comercial"
        elif self.tipoV == 2:
            return "Vuelo en Primera Clase"
        elif self.tipoV == 3:
            return "Vuelo Privado"
        elif self.tipoV == 4:
            return "Vuelo de Enseñanza"
        else:
            return "Vuelo de Carga"

    def imprimirDetalleVuelo(self) -> str:
        return f" Detalles de Vuelo: Origen: {self.origen}, Destino: {self.destino}, Fecha: {self.fecha}, Hora: {self.hora}, Precio: {self.precio}, Tipo de Vuelo: {self.tipoV}, Abordaje: {self.activo}, "

Vuelo4 = Vuelo("Colombia", "Paris", "28-04-2026", "18:00", " $ 1.200.000", 1, "True" )
print(" --------------------------------------------    Vuelo4   --------------------------------------------")
print(Vuelo4.imprimirDetalleVuelo(), Vuelo4.clasificacion_tipoVuelo())
print(" ")

Vuelo5 = Vuelo("Bogota", "Estados Unidos", "15-06-2026", "22:00", " $ 3.000.000", 2, "True" )
print(" --------------------------------------------    Vuelo5   --------------------------------------------")
print(Vuelo5.imprimirDetalleVuelo(), Vuelo5.clasificacion_tipoVuelo())
print(" ")

