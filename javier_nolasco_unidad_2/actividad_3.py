class Vehiculo:
    # Constructor para inicializar los atributos principales del automóvil
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Método para mostrar los detalles completos del vehículo en consola
    def mostrar_detalles(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}')

# Creación de dos objetos de la clase Vehiculo con valores diferentes
vehiculo_uno = Vehiculo("Mazda", "3", "Rojo")
vehiculo_dos = Vehiculo("Ford", "Mustang", "Azul")

# Llamada al método para visualizar la información de cada carro
vehiculo_uno.mostrar_detalles()
vehiculo_dos.mostrar_detalles()