class Usuario:
    # Constructor para inicializar los atributos principales de la persona
    def __init__(self, nombre, edad, ciudad_residencia):
        self.nombre = nombre
        self.edad = edad
        self.ciudad_residencia = ciudad_residencia

    # Método para presentar la información del usuario en consola
    def saludar(self):
        print(f'Hola, me llamo {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad_residencia}.')

# Creación de tres objetos de la clase Usuario con datos de prueba
usuario_uno = Usuario("Carlos", 24, "Guadalajara")
usuario_dos = Usuario("Mariana", 20, "Monterrey")
usuario_tres = Usuario("Fernando", 23, "Querétaro")

# Llamada al método saludar para cada una de las instancias
usuario_uno.saludar()
usuario_dos.saludar()
usuario_tres.saludar()