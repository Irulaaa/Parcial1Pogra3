class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.tiene_cita = False

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.sala_de_espera = []

    def registrar_paciente(self, nombre, motivo_consulta):
    
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                print(f"{nombre} ya tiene una cita. Se le envía a la sala de espera.")
                self.sala_de_espera.append(paciente)
                return
        
        
        nuevo_paciente = Paciente(nombre, motivo_consulta)
        nuevo_paciente.tiene_cita = True
        self.pacientes.append(nuevo_paciente)
        print(f"Se ha registrado a {nombre} para la consulta por {motivo_consulta}.")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            print("Pacientes con citas:")
            for paciente in self.pacientes:
                print(f"- {paciente.nombre}, motivo: {paciente.motivo_consulta}")

    def mostrar_sala_de_espera(self):
        if not self.sala_de_espera:
            print("La sala de espera está vacía.")
        else:
            print("Pacientes en la sala de espera:")
            for paciente in self.sala_de_espera:
                print(f"- {paciente.nombre}, motivo: {paciente.motivo_consulta}")



