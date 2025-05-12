import json
import os
from datetime import datetime, time
from models.turno import Turno

# Configuración de horarios
HORARIO_APERTURA = time(8, 0)  # 8:00 AM
HORARIO_CIERRE = time(18, 0)    # 6:00 PM
ARCHIVO_TURNOS = "data/turnos.json"

class GestorTurnos:
    def __init__(self):
        self.turnos = []  # Inicialización explícita
        self.cargar_turnos()  # Carga los turnos al iniciar

    def cargar_turnos(self):
        """Carga los turnos desde el archivo JSON."""
        try:
            if os.path.exists(ARCHIVO_TURNOS):
                with open(ARCHIVO_TURNOS, "r", encoding="utf-8") as archivo:
                    data = json.load(archivo)
                    self.turnos = [Turno.from_dict(turno_data) for turno_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.turnos = []

    def guardar_turnos(self):
        """Guarda los turnos en el archivo JSON."""
        os.makedirs(os.path.dirname(ARCHIVO_TURNOS), exist_ok=True)  # Crea la carpeta si no existe
        with open(ARCHIVO_TURNOS, "w", encoding="utf-8") as archivo:
            json.dump([turno.to_dict() for turno in self.turnos], archivo, indent=4, ensure_ascii=False)

    def es_dia_laborable(self, fecha):
        """Valida si la fecha es de Lunes a Viernes."""
        return fecha.weekday() < 5  # 0=Lunes, 4=Viernes

    def validar_disponibilidad(self, especialidad, fecha_hora_str):
        """Valida disponibilidad considerando días y horarios."""
        try:
            nueva_fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
            
            # Validar día laborable
            if not self.es_dia_laborable(nueva_fecha_hora):
                return False, "❌ Solo se asignan turnos de Lunes a Viernes"

            # Validar horario de atención
            if not (HORARIO_APERTURA <= nueva_fecha_hora.time() <= HORARIO_CIERRE):
                return False, f"❌ Horario no válido ({HORARIO_APERTURA.strftime('%H:%M')} a {HORARIO_CIERRE.strftime('%H:%M')})"

            # Validar solapamiento
            for turno in self.turnos:
                if (turno.especialidad == especialidad and 
                    turno.fecha_hora == nueva_fecha_hora):
                    return False, "❌ Turno ocupado para esta especialidad"

            return True, "✅ Horario disponible"
        except ValueError:
            return False, "⚠️ Formato inválido (Use: YYYY-MM-DD HH:MM)"

    def registrar_turno(self):
        """Registra un nuevo turno con validación."""
        print("\n--- REGISTRAR NUEVO TURNO ---")
        dni = input("DNI del paciente: ").strip()
        nombre = input("Nombre completo: ").strip()
        especialidad = input("Especialidad médica: ").strip()
        
        while True:
            fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM): ").strip()
            disponible, mensaje = self.validar_disponibilidad(especialidad, fecha_hora)
            print(mensaje)
            if disponible:
                break
            print("Por favor, elija otro horario.\n")

        try:
            nuevo_turno = Turno(dni, nombre, especialidad, fecha_hora)
            self.turnos.append(nuevo_turno)
            self.guardar_turnos()
            print(f"\n✅ Turno registrado:\n{nuevo_turno}")
        except ValueError as e:
            print(f"\n❌ Error: {e}")

    # ... (resto de métodos: listar_turnos, modificar_turno, eliminar_turno)