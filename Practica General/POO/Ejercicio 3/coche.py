class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad = max(0, self.velocidad - 5)

    def mostrar_velocidad(self):
        print(f"{self.marca} {self.modelo} - Velocidad: {self.velocidad} km/h")


# Prueba
c1 = Coche("Toyota", "Corolla")
c2 = Coche("Ford", "Fiesta")

# Acelerar
c1.acelerar()
c1.acelerar()
c2.acelerar()

# Frenar
c1.frenar()
c2.frenar()
c2.frenar()

# Mostrar velocidad
c1.mostrar_velocidad()
c2.mostrar_velocidad()
