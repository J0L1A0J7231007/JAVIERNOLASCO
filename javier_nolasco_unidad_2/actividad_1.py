class CuentaCliente:
    # Atributo de clase para definir la entidad financiera
    nombre_banco = "Banco Central"

    def __init__(self, fondos):
        # Inicializamos el saldo actual del cliente
        self.fondos = fondos

    def mostrar_saldo(self):
        # Muestra en consola el dinero disponible en la cuenta
        print(f'Saldo actual: {self.fondos}')

    @classmethod
    def mostrar_banco(cls):
        # Imprime el nombre de la institución financiera
        print(f'Banco: {cls.nombre_banco}')

    @staticmethod
    def convertir_divisa(dolares):
        # Convierte de dólares a pesos usando un tipo de cambio fijo
        tasa_cambio = 17.46  # Referencia aproximada
        return dolares * tasa_cambio

# Creamos una instancia de la cuenta de prueba
mi_cuenta = CuentaCliente(1000)
mi_cuenta.mostrar_saldo()
mi_cuenta.mostrar_banco()
print("Total convertido:", CuentaCliente.convertir_divisa(6))