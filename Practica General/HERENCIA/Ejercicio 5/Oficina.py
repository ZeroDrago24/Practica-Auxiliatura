# Clase Oficina
class Oficina:
    def __init__(self, nroSillas: int, nroEscritorios: int, nroEstanterias: int):
        self.__nroSillas = nroSillas
        self.__nroEscritorios = nroEscritorios
        self.__nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.__nroSillas}, Escritorios: {self.__nroEscritorios}, Estanterías: {self.__nroEstanterias}")
    
    def cantidadMuebles(self):
        return self.__nroSillas + self.__nroEscritorios + self.__nroEstanterias

# Clase Aula
class Aula:
    def __init__(self, nombre: str, capacidad: int, nroPupitres: int):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroPupitres = nroPupitres

    def mostrar(self):
        print(f"Aula {self.__nombre} - Capacidad: {self.__capacidad}, Pupitres: {self.__nroPupitres}")

    def cantidadMuebles(self):
        return self.__nroPupitres

# Clase Laboratorio
class Laboratorio:
    def __init__(self, nombre: str, capacidad: int, nroMesas: int, nroSillas: int):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroMesas = nroMesas
        self.__nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio {self.__nombre} - Capacidad: {self.__capacidad}, Mesas: {self.__nroMesas}, Sillas: {self.__nroSillas}")
    
    def cantidadMuebles(self):
        return self.__nroMesas + self.__nroSillas

# a) Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio
oficina1 = Oficina(10, 5, 3)
oficina2 = Oficina(12, 6, 4)
aula1 = Aula("Aula 1", 30, 20)
aula2 = Aula("Aula 2", 25, 18)
laboratorio = Laboratorio("Laboratorio 1", 20, 10, 15)

# b) Mostrar datos de cada objeto
oficina1.mostrar()
oficina2.mostrar()
aula1.mostrar()
aula2.mostrar()
laboratorio.mostrar()

# c) Mostrar la cantidad de muebles de cada ambiente
print("\nCantidad de muebles:")
print(f"Oficina 1: {oficina1.cantidadMuebles()}")
print(f"Oficina 2: {oficina2.cantidadMuebles()}")
print(f"Aula 1: {aula1.cantidadMuebles()}")
print(f"Aula 2: {aula2.cantidadMuebles()}")
print(f"Laboratorio: {laboratorio.cantidadMuebles()}")
