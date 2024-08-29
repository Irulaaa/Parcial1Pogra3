class Vehiculo:
    def __init__(self, marca, modelo, tipo, costo_por_dia):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.costo_por_dia = costo_por_dia

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Renta:
    def __init__(self, vehiculo, cliente, dias_renta):
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.dias_renta = dias_renta

    def calcular_costo(self):
        return self.vehiculo.costo_por_dia * self.dias_renta

    def imprimir_factura(self):
        print(f"Factura para {self.cliente.nombre}:")
        print(f"Vehículo: {self.vehiculo.marca} {self.vehiculo.modelo} ({self.vehiculo.tipo})")
        print(f"Días de renta: {self.dias_renta}")
        print(f"Total a pagar: ${self.calcular_costo()}")

