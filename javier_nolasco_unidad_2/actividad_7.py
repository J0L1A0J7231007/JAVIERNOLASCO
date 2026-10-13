# Act 4. Create a class Engine with a method start() that prints "Engine started".
# Create a class Car that has an attribute engine (type Engine) and a method start_car() that calls engine.start().

class Motor:
    # Clase que representa el componente del motor
    def encender(self):
        print("Motor encendido correctamente.")

class Automovil:
    # Clase que contiene una instancia de Motor mediante composición
    def __init__(self):
        self.motor = Motor()

    def arrancar_auto(self):
        # Llama al método del atributo motor
        print("Iniciando secuencia del vehículo...")
        self.motor.encender()


mi_vehiculo = Automovil()
mi_vehiculo.arrancar_auto()