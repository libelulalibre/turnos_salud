from datetime import datetime
from typing import Optional

class Turno:
    def __init__(self, dni: str, nombre: str, especialidad: str, fecha_hora: str, estado: str = "pendiente", id_turno: int = None):
        """
        Constructor modificado para ser compatible con versiones anteriores
        Si id_turno es None, se generará automáticamente al guardar
        """
        self.id_turno = id_turno  # Puede ser None inicialmente
        self.dni = dni.strip()
        self.nombre = nombre.strip()
        self.especialidad = especialidad.strip()
        self.fecha_hora = self._validar_fecha(fecha_hora)
        self.estado = estado.lower()

    def _validar_fecha(self, fecha_str: str):
        try:
            return datetime.strptime(fecha_str.strip(), "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use: YYYY-MM-DD HH:MM")

    def __str__(self):
        id_display = f"ID: {self.id_turno} | " if self.id_turno is not None else ""
        return (
            f"{id_display}Paciente: {self.nombre} (DNI: {self.dni})\n"
            f"Especialidad: {self.especialidad} | Fecha: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}\n"
            f"Estado: {self.estado.capitalize()}\n{'-'*40}"
        )

    def to_dict(self):
        """Convierte el turno a diccionario, incluyendo el ID si existe"""
        data = {
            "dni": self.dni,
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "fecha_hora": self.fecha_hora.strftime("%Y-%m-%d %H:%M"),
            "estado": self.estado
        }
        if self.id_turno is not None:
            data["id_turno"] = self.id_turno
        return data

    @classmethod
    def from_dict(cls, data: dict):
        """Crea un Turno desde diccionario, compatible con versiones sin ID"""
        return cls(
            dni=data["dni"],
            nombre=data["nombre"],
            especialidad=data["especialidad"],
            fecha_hora=data["fecha_hora"],
            estado=data.get("estado", "pendiente"),
            id_turno=data.get("id_turno")  # Usa get() para evitar KeyError
        )