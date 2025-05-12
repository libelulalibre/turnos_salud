from controllers.gestor_turnos import GestorTurnos

def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE TURNOS ---")
    print("1. Registrar turno")
    print("2. Listar turnos")
    print("3. Modificar turno")
    print("4. Eliminar turno")
    print("5. Salir")

def main():
    gestor = GestorTurnos()
    
    # Datos de ejemplo (opcional)
    # gestor.crear_turno("12345678", "Juan Pérez", "Cardiología", "2025-05-10 10:30")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            gestor.registrar_turno()  # Cambiado a registrar_turno que pide inputs
        elif opcion == "2":
            gestor.listar_turnos()
        elif opcion == "3":
            gestor.modificar_turno()
        elif opcion == "4":
            gestor.eliminar_turno()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()