class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche

class ServicioExtra:
    def __init__(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo

class Reserva:
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.servicios_extra = []

    def agregar_servicio_extra(self, servicio):
        self.servicios_extra.append(servicio)

    def calcular_total(self):
        total = self.habitacion.precio_por_noche * self.noches
        for servicio in self.servicios_extra:
            total += servicio.costo
        return total

    def imprimir_factura(self):
        print(f"Factura para {self.cliente.nombre}:")
        print(f"Habitación {self.habitacion.tipo} - ${self.habitacion.precio_por_noche} por noche")
        print(f"Noches: {self.noches}")
        if self.servicios_extra:
            print("Servicios extra:")
            for servicio in self.servicios_extra:
                print(f"- {servicio.descripcion}: ${servicio.costo}")
        print(f"Total a pagar: ${self.calcular_total()}")


