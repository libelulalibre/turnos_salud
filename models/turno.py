# models/turno.py

from datetime import datetime

class Turno:
    def __init__(self, id_turno, paciente, especialidad, fecha_hora, estado="pendiente"):
        self.id_turno = id_turno  # identificador único
        self.paciente = paciente
        self.especialidad = especialidad
        self.fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        self.estado = estado

    def __str__(self):
        return f"Turno #{self.id_turno} - {self.paciente} ({self.especialidad}) - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} - Estado: {self.estado}"

    def to_dict(self):
        """Convierte el objeto en un diccionario serializable a JSON."""
        return {
            "id_turno": self.id_turno,
            "paciente": self.paciente,
            "especialidad": self.especialidad,
            "fecha_hora": self.fecha_hora.strftime("%Y-%m-%d %H:%M"),
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Turno a partir de un diccionario."""
        return cls(
            id_turno=data["id_turno"],
            paciente=data["paciente"],
            especialidad=data["especialidad"],
            fecha_hora=data["fecha_hora"],
            estado=data["estado"]
        )

class Turno:
    def __init__(self, id_turno, id_paciente, fecha, hora, especialidad, estado="activo"):
        self.id_turno = id_turno
        self.id_paciente = id_paciente
        self.fecha = fecha  # Ej: '2025-05-10'
        self.hora = hora    # Ej: '14:30'
        self.especialidad = especialidad
        self.estado = estado  # Por defecto "activo"

    def to_dict(self):
        """Convierte el objeto en un diccionario para guardarlo en JSON"""
        return {
            "id_turno": self.id_turno,
            "id_paciente": self.id_paciente,
            "fecha": self.fecha,
            "hora": self.hora,
            "especialidad": self.especialidad,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Turno a partir de un diccionario (desde JSON)"""
        return Turno(
            data["id_turno"],
            data["id_paciente"],
            data["fecha"],
            data["hora"],
            data["especialidad"],
            data.get("estado", "activo")  # Usa "activo" si no viene en el JSON
        )

