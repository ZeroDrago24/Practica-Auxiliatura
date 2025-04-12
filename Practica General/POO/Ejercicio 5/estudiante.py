class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def verificar_aprobado(self):
        return self.calcular_promedio() >= 6

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        estado = "Aprobado" if self.verificar_aprobado() else "Reprobado"
        print(f"{self.nombre} - Promedio: {promedio:.2f} - {estado}")


# Crear 3 estudiantes
e1 = Estudiante("Lucía", 8, 7)
e2 = Estudiante("Carlos", 5, 6)
e3 = Estudiante("Ana", 4, 5)

print("=== Información de Estudiantes ===")
for estudiante in [e1, e2, e3]:
    estudiante.mostrar_info()
