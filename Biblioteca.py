from datetime import datetime, timedelta

class Tarjeta:
    def __init__(self, nombre_persona):
        self.nombre_persona = nombre_persona

class Prestamo:
    def __init__(self, libro, tarjeta, dias_prestamo):
        self.libro = libro
        self.tarjeta = tarjeta
        self.fecha_retiro = datetime.now()
        self.fecha_devolucion = self.fecha_retiro + timedelta(days=dias_prestamo)
        self.devuelto = False

    def devolver_libro(self):
        fecha_actual = datetime.now()
        if fecha_actual > self.fecha_devolucion:
            print(f"El libro '{self.libro}' se ha devuelto tarde. Se aplicará una sanción.")
        else:
            print(f"El libro '{self.libro}' se ha devuelto a tiempo. No se aplicará sanción.")
        self.devuelto = True


tarjeta = Tarjeta("Ana Gómez")
prestamo = Prestamo("Cien años de soledad", tarjeta, 7)


prestamo.devolver_libro()
