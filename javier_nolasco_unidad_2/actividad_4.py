# Act 1. Create a class Employee with attributes name and salary, and a method show_info() that prints the name and salary.
# Then, create a class Manager that inherits from Employee and adds an attribute department.
# Override show_info() to also display the department.

class Empleado:
    # Clase base para representar a un trabajador
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_info(self):
        # Muestra la información básica del empleado
        print(f'Empleado: {self.nombre}, Sueldo: ${self.sueldo}')

class Gerente(Empleado):
    # Clase derivada que hereda de Empleado y agrega departamento
    def __init__(self, nombre, sueldo, area_trabajo):
        # Llama al constructor de la clase base
        super().__init__(nombre, sueldo)
        self.area_trabajo = area_trabajo

    def mostrar_info(self):
        # Sobrescribe el método para incluir el departamento
        print(f'Gerente: {self.nombre}, Sueldo: ${self.sueldo}, Área: {self.area_trabajo}')


empleado_base = Empleado("Laura", 15000)
gerente_area = Gerente("Roberto", 32000, "Sistemas")

empleado_base.mostrar_info()
gerente_area.mostrar_info()