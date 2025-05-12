from datetime import datetime
from typing import Optional

class Turno:
    def __init__(
        self,
        dni: str,
        nombre: str,
        especialidad: str,
        fecha_hora: str,  # Formato: "YYYY-MM-DD HH:MM"
        estado: str = "pendiente",
    ):
        self.dni = dni.strip()
        self.nombre = nombre.strip()
        self.especialidad = especialidad.strip()
        self.fecha_hora = self._validar_fecha(fecha_hora)
        self.estado = estado.lower()

    def _validar_fecha(self, fecha_str: str) -> datetime:
        """Convierte y valida el formato de fecha."""
        try:
            return datetime.strptime(fecha_str.strip(), "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError(f"Formato de fecha inválido. Use: YYYY-MM-DD HH:MM. Error: {e}")

    def __str__(self) -> str:
        """Representación legible del turno."""
        return (
            f"Turno - {self.nombre} (DNI: {self.dni})\n"
            f"Especialidad: {self.especialidad}\n"
            f"Fecha/Hora: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}\n"
            f"Estado: {self.estado}"
        )

    def to_dict(self) -> dict:
        """Convierte el turno a un diccionario para guardar en JSON."""
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "fecha_hora": self.fecha_hora.strftime("%Y-%m-%d %H:%M"),
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Turno":
        """Crea un Turno desde un diccionario (para cargar desde JSON)."""
        return cls(
            dni=data["dni"],
            nombre=data["nombre"],
            especialidad=data["especialidad"],
            fecha_hora=data["fecha_hora"],
            estado=data.get("estado", "pendiente"),
        )