from src.gestor import GestorClientes


def mostrar_menu():
    print("\n===== AXANET - Gestión de Clientes =====")
    print("1. Crear cliente")
    print("2. Buscar cliente")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Listar clientes")
    print("0. Salir")


def main():
    gestor = GestorClientes()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            telefono = input("Teléfono: ").strip()
            direccion = input("Dirección: ").strip()
            gestor.crear_cliente(nombre, correo, telefono, direccion)

        elif opcion == "2":
            nombre = input("Nombre del cliente a buscar: ").strip()
            gestor.buscar_cliente(nombre)

        elif opcion == "3":
            nombre = input("Nombre del cliente a actualizar: ").strip()
            if nombre not in gestor.clientes:
                gestor.buscar_cliente(nombre)
                continue

            print("Deje en blanco los campos que no desea modificar.")
            correo = input("Nuevo correo: ").strip()
            telefono = input("Nuevo teléfono: ").strip()
            direccion = input("Nueva dirección: ").strip()
            gestor.actualizar_cliente(
                nombre,
                correo=correo or None,
                telefono=telefono or None,
                direccion=direccion or None,
            )

        elif opcion == "4":
            nombre = input("Nombre del cliente a eliminar: ").strip()
            gestor.eliminar_cliente(nombre)

        elif opcion == "5":
            gestor.listar_clientes()

        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
