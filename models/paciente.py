class Paciente:
    def __init__(self, id_paciente, nombre, dni, especialidad):
        self.id_paciente = id_paciente  
        self.nombre = nombre
        self.dni = dni  
        self.especialidad = especialidad  

    def to_dict(self):
        """Convierte el objeto en un diccionario para guardarlo en JSON"""
        return {
            "id_paciente": self.id_paciente,
            "nombre": self.nombre,
            "dni": self.dni,
            "especialidad": self.especialidad
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Paciente a partir de un diccionario (desde JSON)"""
        return Paciente(
            data["id_paciente"],
            data["nombre"],
            data["dni"],
            data["especialidad"]
        )


