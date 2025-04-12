class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def es_mayor_edad(self):
        return self.edad >= 18


# Prueba
persona1 = Persona("Ana", 22, "La Paz")
persona2 = Persona("Luis", 17, "Cochabamba")
persona3 = Persona("Marta", 30, "Santa Cruz")

personas = [persona1, persona2, persona3]

for p in personas:
    p.saludar()
    print("Mayor de edad:", "Sí" if p.es_mayor_edad() else "No")
    print("---")
