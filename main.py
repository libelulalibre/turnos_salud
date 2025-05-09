from controllers.gestor_turnos import GestorTurnos

gestor = GestorTurnos()

while True:
    print("\n--- MENÚ DE GESTIÓN DE TURNOS ---")
    print("1. Registrar turno")
    print("2. Listar turnos")
    print("3. Modificar turno")
    print("4. Eliminar turno")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        gestor.registrar_turno()
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
