 
class Cocinero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora

    # Método para obtener el sueldo total (sueldos + horas extra)
    def sueldoTotal(self):
        return self.__sueldoMes + (self.__horasExtra * self.__sueldoHora)

     
    def getSueldoMes(self):
        return self.__sueldoMes
 
    def mostrarSueldoMesIgual(self, sueldo: int):
        if self.__sueldoMes == sueldo:
            print(f"Empleado: {self.__nombre} - SueldoMes: {self.__sueldoMes}")

 
class Mesero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float, propina: float):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora
        self.__propina = propina

    # Método para obtener el sueldo total (sueldos + horas extra + propina)
    def sueldoTotal(self):
        return self.__sueldoMes + (self.__horasExtra * self.__sueldoHora) + self.__propina

     
    def getSueldoMes(self):
        return self.__sueldoMes

    
    def mostrarSueldoMesIgual(self, sueldo: int):
        if self.__sueldoMes == sueldo:
            print(f"Empleado: {self.__nombre} - SueldoMes: {self.__sueldoMes}")

 
class Administrativo:
    def __init__(self, nombre: str, sueldoMes: float, cargo: str):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__cargo = cargo
 
    def sueldoTotal(self):
        return self.__sueldoMes

    
    def getSueldoMes(self):
        return self.__sueldoMes

    # Método para mostrar los empleados con sueldoMes igual a un valor dado
    def mostrarSueldoMesIgual(self, sueldo: float):
        if self.__sueldoMes == sueldo:
            print(f"Empleado: {self.__nombre} - SueldoMes: {self.__sueldoMes} - Cargo: {self.__cargo}")


# a) Instanciar 1 Cocinero, 2 Meseros y 2 Administrativos
cocinero = Cocinero("Juan", 2000, 10, 15.50)
mesero1 = Mesero("Pedro", 1500, 20, 10, 100)
mesero2 = Mesero("Ana", 1400, 15, 9, 120)
administrativo1 = Administrativo("Carlos", 1800, "Gerente")
administrativo2 = Administrativo("Maria", 1800, "Secretaria")

# b) Sobrecargar el método SueldoTotal para mostrar el sueldo total
print(f"Sueldo total del Cocinero: {cocinero.sueldoTotal()}")
print(f"Sueldo total de Mesero 1: {mesero1.sueldoTotal()}")
print(f"Sueldo total de Mesero 2: {mesero2.sueldoTotal()}")
print(f"Sueldo total Administrativo 1: {administrativo1.sueldoTotal()}")
print(f"Sueldo total Administrativo 2: {administrativo2.sueldoTotal()}")

# c) Sobrecargar el método para mostrar empleados con sueldoMes igual a un valor X
print("\nEmpleados con SueldoMes igual a 1800:")
cocinero.mostrarSueldoMesIgual(1800)
mesero1.mostrarSueldoMesIgual(1800)
mesero2.mostrarSueldoMesIgual(1800)
administrativo1.mostrarSueldoMesIgual(1800)
administrativo2.mostrarSueldoMesIgual(1800)
