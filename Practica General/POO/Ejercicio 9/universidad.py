class Universidad:
    def __init__(self, nombre, carreras, cantidad_estudiantes):
        self.nombre = nombre
        self.carreras = carreras
        self.cantidad_estudiantes = cantidad_estudiantes

    def get_nombre(self):
        return self.nombre

    def get_carreras(self):
        return self.carreras

    def get_cantidad_estudiantes(self):
        return self.cantidad_estudiantes

# Crear universidades
u1 = Universidad("UMSA", ["Informática", "Matemáticas", "Física"], 5000)
u2 = Universidad("UCB", ["Informática", "Derecho", "Administración", "Arquitectura"], 3000)
u3 = Universidad("UPB", ["Electrónica", "Administración", "Informática"], 2500)

# a) Universidad con más carreras
universidades = [u1, u2, u3]
mayor = max(universidades, key=lambda u: len(u.get_carreras()))
print(f"Universidad con más carreras: {mayor.get_nombre()}")

# b) Carreras en común entre UMSA y UCB
print(f"Carreras en común entre {u1.get_nombre()} y {u2.get_nombre()}:")
comunes = set(u1.get_carreras()).intersection(u2.get_carreras())
for c in comunes:
    print("- " + c)

# c) Total de estudiantes
total = sum(u.get_cantidad_estudiantes() for u in universidades)
print(f"Total de estudiantes: {total}")
