import json
import os
from datetime import datetime, time
from models.turno import Turno

# Horario disponible
HORARIO_APERTURA = time(8, 0)  
HORARIO_CIERRE = time(18, 0)    
ARCHIVO_TURNOS = "data/turnos.json"

import json
import os
from datetime import datetime, time
from models.turno import Turno

HORARIO_APERTURA = time(8, 0)  
HORARIO_CIERRE = time(18, 0)    
ARCHIVO_TURNOS = "data/turnos.json"

class GestorTurnos:
    def __init__(self):
        self.turnos = []  
        self.cargar_turnos()
        self.proximo_id = self._calcular_proximo_id()

    def _calcular_proximo_id(self):
        """Calcula el próximo ID disponible, asignando IDs a turnos sin ID"""
        if not self.turnos:
            return 1
        
        # Asignar IDs a turnos que no lo tengan
        max_id = 0
        for turno in self.turnos:
            if turno.id_turno is None:
                max_id += 1
                turno.id_turno = max_id
            elif turno.id_turno > max_id:
                max_id = turno.id_turno
        
        # Guardar los cambios si hubo turnos sin ID
        if any(turno.id_turno is None for turno in self.turnos):
            self.guardar_turnos()
        
        return max_id + 1

    def cargar_turnos(self):
        """Carga los turnos desde el archivo JSON, compatible con versiones anteriores"""
        try:
            if os.path.exists(ARCHIVO_TURNOS):
                with open(ARCHIVO_TURNOS, "r", encoding="utf-8") as archivo:
                    data = json.load(archivo)
                    self.turnos = [Turno.from_dict(turno_data) for turno_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.turnos = []
            
    def guardar_turnos(self):
        """Guarda los turnos en el archivo JSON."""
        os.makedirs(os.path.dirname(ARCHIVO_TURNOS), exist_ok=True)  
        with open(ARCHIVO_TURNOS, "w", encoding="utf-8") as archivo:
            json.dump([turno.to_dict() for turno in self.turnos], archivo, indent=4, ensure_ascii=False)

    def es_dia_laborable(self, fecha):
        """Valida si la fecha es de Lunes a Viernes."""
        return fecha.weekday() < 5 

    def validar_disponibilidad(self, especialidad, fecha_hora_str):
        """Valida disponibilidad considerando días y horarios."""
        try:
            nueva_fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
            
            # Validar día 
            if not self.es_dia_laborable(nueva_fecha_hora):
                return False, "❌ Solo se asignan turnos de Lunes a Viernes"

            # Validar horario 
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
            nuevo_turno = Turno(
                id_turno=self.proximo_id,  # Nuevo: asignación de ID
                dni=dni,
                nombre=nombre,
                especialidad=especialidad,
                fecha_hora=fecha_hora
            )
            self.turnos.append(nuevo_turno)
            self.proximo_id += 1  # Incrementar para el próximo turno
            self.guardar_turnos()
            print(f"\n✅ Turno registrado con ID: {nuevo_turno.id_turno}")
        except ValueError as e:
            print(f"\n❌ Error: {e}")

    def listar_turnos(self):
        """Muestra todos los turnos registrados"""
        if not self.turnos:
            print("\nNo hay turnos registrados.")
            return
    
        print("\n--- LISTADO DE TURNOS ---")
        for turno in self.turnos:
            print(turno)  # Ahora muestra el ID que viene del objeto Turno

    def modificar_turno(self):
        """Modifica un turno existente"""
        if not self.turnos:
            print("\nNo hay turnos para modificar.")
            return
    
        self.listar_turnos()
        try:
            id_turno = int(input("\nIngrese el ID del turno a modificar: "))
            turno = next((t for t in self.turnos if t.id_turno == id_turno), None)
            
            if not turno:
                print("❌ ID de turno no encontrado.")
                return
        
            print(f"\nEditando turno ID {turno.id_turno}:\n{turno}")
        
            nueva_especialidad = input("Nueva especialidad (dejar vacío para mantener): ").strip()
            nueva_fecha = input("Nueva fecha y hora (YYYY-MM-DD HH:MM, vacío para mantener): ").strip()
            nuevo_estado = input("Nuevo estado (pendiente/confirmado/cancelado): ").strip().lower()
        
            if nueva_especialidad:
                turno.especialidad = nueva_especialidad
            if nueva_fecha:
                turno.fecha_hora = datetime.strptime(nueva_fecha, "%Y-%m-%d %H:%M")
            if nuevo_estado in ("pendiente", "confirmado", "cancelado"):
                turno.estado = nuevo_estado
        
            self.guardar_turnos()
            print("\n✅ Turno modificado correctamente.")
        except ValueError:
            print("\n⚠️ Formato de fecha incorrecto. Use YYYY-MM-DD HH:MM.")

    def eliminar_turno(self):
        """Elimina un turno existente"""
        if not self.turnos:
            print("\nNo hay turnos para eliminar.")
            return
    
        self.listar_turnos()
        try:
            id_turno = int(input("\nIngrese el ID del turno a eliminar: "))
            turno = next((t for t in self.turnos if t.id_turno == id_turno), None)
            
            if not turno:
                print("❌ ID de turno no encontrado.")
                return
        
            self.turnos = [t for t in self.turnos if t.id_turno != id_turno]
            self.guardar_turnos()
            print(f"\n🗑️ Turno ID {id_turno} eliminado correctamente.")
        except ValueError:
            print("\n⚠️ Ingrese un ID válido.")