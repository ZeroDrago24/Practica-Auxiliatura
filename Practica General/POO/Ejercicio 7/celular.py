class Aplicacion:
    def __init__(self, nombre, tamano_mb):
        self.nombre = nombre
        self.tamano_mb = tamano_mb

class Celular:
    def __init__(self):
        self.aplicaciones = []
        self.espacio_disponible = 1024
        self.bateria = 100.0

    def instalar_aplicacion(self, app):
        if len(self.aplicaciones) >= 20:
            print("No se pueden instalar más de 20 aplicaciones.")
        elif self.espacio_disponible >= app.tamano_mb:
            self.aplicaciones.append(app)
            self.espacio_disponible -= app.tamano_mb
            print(f"Aplicación '{app.nombre}' instalada.")
        else:
            print("No hay suficiente espacio.")

    def usar_aplicacion(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado")
            return
        for app in self.aplicaciones:
            if app.nombre == nombre:
                if app.tamano_mb > 250:
                    consumo = 5
                elif app.tamano_mb > 100:
                    consumo = 2
                else:
                    consumo = 1
                gasto = (minutos // 10) * consumo
                if self.bateria - gasto <= 0:
                    self.bateria = 0
                    print("Batería agotada. Celular apagado")
                else:
                    self.bateria -= gasto
                    print(f"Usando {nombre} por {minutos} minutos. Batería restante: {self.bateria:.2f}%")
                return
        print("Aplicación no encontrada.")

    def mostrar_bateria(self):
        print(f"Batería: {self.bateria:.2f}%")


# Ejemplo de uso
cel = Celular()
app1 = Aplicacion("WhatsApp", 120)
app2 = Aplicacion("YouTube", 300)
app3 = Aplicacion("Notas", 80)

cel.instalar_aplicacion(app1)
cel.instalar_aplicacion(app2)
cel.instalar_aplicacion(app3)

cel.usar_aplicacion("YouTube", 30)
cel.usar_aplicacion("Notas", 20)
cel.mostrar_bateria()
