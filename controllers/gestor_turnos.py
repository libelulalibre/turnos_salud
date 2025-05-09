import json
import os
from models.turno import Turno
from models.paciente import Paciente

ARCHIVO_TURNOS = "data/turnos.json"

class GestorTurnos:
    def __init__(self):
        self.turnos = self.cargar_turnos()

    def cargar_turnos(self):
        if not os.path.exists(ARCHIVO_TURNOS):
            return []
        with open(ARCHIVO_TURNOS, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            return [Turno.from_dict(item) for item in data]

    def guardar_turnos(self):
        with open(ARCHIVO_TURNOS, "w", encoding="utf-8") as archivo:
            json.dump([turno.to_dict() for turno in self.turnos], archivo, indent=4, ensure_ascii=False)

    def crear_turno(self):
        """Crea y guarda un nuevo turno con los datos del paciente incluidos"""
        print("\n Registro de nuevo turno")

        nombre = input("Nombre del paciente: ")
        dni = input("DNI del paciente: ")
        telefono = input("Teléfono del paciente: ")
        especialidad = input("Especialidad: ")
        fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM): ")

        paciente = Paciente(nombre, dni, telefono)

        if self.turnos:
            ultimo_id = max(t.id_turno for t in self.turnos)
        else:
            ultimo_id = 0

        nuevo_id = ultimo_id + 1
        nuevo_turno = Turno(nuevo_id, paciente, especialidad, fecha_hora)
        self.turnos.append(nuevo_turno)
        self.guardar_turnos()
        print(f"\n✅ Turno creado correctamente:\n{nuevo_turno}")

    def listar_turnos(self):
        """Muestra todos los turnos registrados."""
        if not self.turnos:
            print("\n📭 No hay turnos registrados.")
            return

        print("\n📋 Lista de turnos registrados:")
        for turno in self.turnos:
            print(turno)

    def modificar_turno(self):
        """Modifica los datos de un turno existente."""
        if not self.turnos:
            print("\n📭 No hay turnos para modificar.")
            return

        try:
            id_turno = int(input("🔎 Ingrese el ID del turno a modificar: "))
            turno = next((t for t in self.turnos if t.id_turno == id_turno), None)

            if not turno:
                print("❌ Turno no encontrado.")
                return

            print(f"✏️ Modificando turno:\n{turno}")
            nueva_especialidad = input("Nueva especialidad (dejar vacío para mantener): ")
            nueva_fecha = input("Nueva fecha y hora (YYYY-MM-DD HH:MM, dejar vacío para mantener): ")
            nuevo_estado = input("Nuevo estado (pendiente, confirmado, cancelado): ")

            if nueva_especialidad:
                turno.especialidad = nueva_especialidad
            if nueva_fecha:
                from datetime import datetime
                turno.fecha_hora = datetime.strptime(nueva_fecha, "%Y-%m-%d %H:%M")
            if nuevo_estado:
                turno.estado = nuevo_estado

            self.guardar_turnos()
            print("✅ Turno modificado correctamente.\n")

        except ValueError:
            print("⚠️ Entrada inválida. Intente de nuevo.")
