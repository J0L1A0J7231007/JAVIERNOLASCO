# Act 2. Create a class Accountant with a method generate_report() that prints "Generating financial report".
# Create a class Technician with a method repair_machine() that prints "Repairing machine".
# Create a class Boss that inherits from both classes and test both methods.

class Contador:
    # Clase que maneja tareas financieras
    def generar_reporte(self):
        print("Generando reporte financiero...")

class Tecnico:
    # Clase que maneja soporte y reparaciones
    def reparar_maquina(self):
        print("Reparando equipo de cómputo...")

class Jefatura(Contador, Tecnico):
    # Clase que hereda las habilidades de Contador y Tecnico (Herencia múltiple)
    pass


jefe_de_area = Jefatura()
jefe_de_area.generar_reporte()
jefe_de_area.reparar_maquina()