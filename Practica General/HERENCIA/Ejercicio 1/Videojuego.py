# Clase Videojuego con atributos nombre, plataforma y cantidadJugadores
class Videojuego:
    # Constructor 1: Inicializa nombre, plataforma y cantidadJugadores
    def __init__(self, nombre: str, plataforma: str, cantidadJugadores: int = 1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    # Constructor 2 (método de clase) que usa solo dos parámetros (nombre, plataforma) y asigna 1 jugador por defecto
    @classmethod
    def crear_videojuego(cls, nombre: str, plataforma: str):
        return cls(nombre, plataforma, 1)

    # Método para mostrar los detalles del videojuego
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de Jugadores: {self.cantidadJugadores}")

    # Método para agregar jugadores
    # Si no se pasa un argumento, agrega 1 jugador
    def agregarJugadores(self, jugadores: int = 1):
        self.cantidadJugadores += jugadores

# a) Instanciar dos videojuegos
# Usando el constructor normal (con 3 parámetros)
videojuego1 = Videojuego("Zelda", "Switch", 2)

# Usando el método de clase (con 2 parámetros)
videojuego2 = Videojuego.crear_videojuego("Minecraft", "PC")

# b) Sobrecargar el constructor 2 veces
# - Un constructor que recibe tres parámetros (nombre, plataforma, cantidadJugadores)
# - Un constructor que recibe solo dos parámetros (nombre, plataforma) y asigna 1 jugador

# c) Mostrar los videojuegos
videojuego1.mostrar()
videojuego2.mostrar()

# d) Sobrecargar el método agregarJugadores
# Agregar 1 jugador a videojuego1 (por defecto)
videojuego1.agregarJugadores()
videojuego1.mostrar()

# Agregar 3 jugadores a videojuego2
videojuego2.agregarJugadores(3)
videojuego2.mostrar()
