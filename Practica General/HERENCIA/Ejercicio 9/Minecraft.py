# Clase BloqueCofre
class BloqueCofre:
    def __init__(self, capacidad: int, resistencia: int, tipo: str):
        self.__capacidad = capacidad
        self.__resistencia = resistencia
        self.__tipo = tipo

    def accion(self):
        print(f"Acción del {self.__tipo} con capacidad {self.__capacidad} y resistencia {self.__resistencia}.")
    
    def colocar(self, orientacion: str):
        print(f"Colocando el {self.__tipo} en la orientación {orientacion}.")
    
    def romper(self):
        print(f"Rompiendo el {self.__tipo}.")

# Clase BloqueTnt
class BloqueTnt:
    def __init__(self, tipo: str, daño: int):
        self.__tipo = tipo
        self.__daño = daño

    def accion(self):
        print(f"Acción del {self.__tipo} con daño {self.__daño}.")
    
    def colocar(self, orientacion: str):
        print(f"Colocando el {self.__tipo} en la orientación {orientacion}.")
    
    def romper(self):
        print(f"Rompiendo el {self.__tipo}, ¡¡BOOM!!")

# Clase BloqueHorno
class BloqueHorno:
    def __init__(self, color: str, capacidadComida: int):
        self.__color = color
        self.__capacidadComida = capacidadComida

    def accion(self):
        print(f"Acción del {self.__color} Horno con capacidad de comida {self.__capacidadComida}.")
    
    def colocar(self, orientacion: str):
        print(f"Colocando el Horno de color {self.__color} en la orientación {orientacion}.")
    
    def romper(self):
        print(f"Rompiendo el Horno de color {self.__color}, ¡se destruye!")

# a) Crear e instanciar bloques
bloqueCofre = BloqueCofre(50, 100, "Cofre")
bloqueTnt = BloqueTnt("TNT", 200)
bloqueHorno = BloqueHorno("Gris", 10)

# b) Sobrescribir la acción de cada bloque
bloqueCofre.accion()
bloqueTnt.accion()
bloqueHorno.accion()

# c) Colocar bloques en distintas orientaciones
bloqueCofre.colocar("suelo")
bloqueTnt.colocar("pared")
bloqueHorno.colocar("techo")

# d) Romper bloques
bloqueCofre.romper()
bloqueTnt.romper()
bloqueHorno.romper()
