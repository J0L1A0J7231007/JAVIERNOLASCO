# Act 3. Create a function calculate_payment(worker) that calls a method payment() of the passed object.
# Create several classes (FullTimeEmployee, HourlyEmployee) each with its own payment() method.
# Test the function with different objects and see how the same method produces different results.

class EmpleadoTiempoCompleto:
    # Empleado con sueldo mensual fijo
    def __init__(self, salario_fijo):
        self.salario_fijo = salario_fijo

    def calcular_pago(self):
        return self.salario_fijo

class EmpleadoPorHoras:
    # Empleado cuyo sueldo depende de las horas laboradas
    def __init__(self, horas_trabajadas, tarifa_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa_hora

def procesar_pago(trabajador):
    # Función polimórfica que ejecuta calcular_pago independientemente del tipo de empleado
    monto = trabajador.calcular_pago()
    print(f'Monto a pagar al colaborador: ${monto}')


trabajador_planta = EmpleadoTiempoCompleto(18000)
trabajador_eventual = EmpleadoPorHoras(40, 150)

procesar_pago(trabajador_planta)
procesar_pago(trabajador_eventual)