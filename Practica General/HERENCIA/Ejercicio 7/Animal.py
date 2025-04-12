# Clase Perro
class Perro:
    def __init__(self, nombre: str, edad: int, raza: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza

    def hacerSonido(self):
        print(f"{self.__nombre} dice: ¡Guau!")

    def moverse(self):
        print(f"{self.__nombre} corre.")

# Clase Gato
class Gato:
    def __init__(self, nombre: str, color: str):
        self.__nombre = nombre
        self.__color = color

    def hacerSonido(self):
        print(f"{self.__nombre} dice: ¡Miau!")

    def moverse(self):
        print(f"{self.__nombre} salta.")

# Clase Pajaro
class Pajaro:
    def __init__(self, nombre: str, tipo: str):
        self.__nombre = nombre
        self.__tipo = tipo

    def hacerSonido(self):
        print(f"{self.__nombre} dice: ¡Pio!")

    def moverse(self):
        print(f"{self.__nombre} vuela.")

# a) Instanciar 1 Perro, 1 Gato y 1 Pájaro
perro = Perro("Rex", 5, "Pastor Alemán")
gato = Gato("Mia", "Blanco")
pajaro = Pajaro("Piolin", "Canario")

# b) Hacer que cada animal emita su sonido
perro.hacerSonido()
gato.hacerSonido()
pajaro.hacerSonido()

# c) Indicar cómo se mueve cada animal
perro.moverse()
gato.moverse()
pajaro.moverse()
