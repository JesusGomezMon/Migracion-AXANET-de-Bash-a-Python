import json
import os

from src.cliente import Cliente


class GestorClientes:
    def __init__(self, ruta_json="data/clientes.json"):
        self.ruta_json = ruta_json
        self.clientes = {}
        self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.ruta_json):
            os.makedirs(os.path.dirname(self.ruta_json), exist_ok=True)
            self._guardar_datos()
            return

        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.clientes = datos

    def _guardar_datos(self):
        os.makedirs(os.path.dirname(self.ruta_json), exist_ok=True)
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(self.clientes, archivo, indent=4, ensure_ascii=False)

    def _siguiente_id(self):
        if not self.clientes:
            return 1

        ids = [info["id"] for info in self.clientes.values()]
        return max(ids) + 1

    def crear_cliente(self, nombre, correo, telefono, direccion):
        if nombre in self.clientes:
            print(f"Error: ya existe un cliente con el nombre '{nombre}'.")
            return False

        cliente = Cliente(
            self._siguiente_id(), nombre, correo, telefono, direccion
        )
        self.clientes[nombre] = cliente.to_dict()
        self._guardar_datos()
        print(f"Cliente '{nombre}' creado correctamente.")
        return True

    def buscar_cliente(self, nombre):
        if nombre not in self.clientes:
            print(f"No se encontró el cliente '{nombre}'.")
            return None

        info = self.clientes[nombre]
        print(f"\n--- Cliente: {nombre} ---")
        print(f"ID: {info['id']}")
        print(f"Correo: {info['correo']}")
        print(f"Teléfono: {info['telefono']}")
        print(f"Dirección: {info['direccion']}")
        return info

    def actualizar_cliente(
        self, nombre, correo=None, telefono=None, direccion=None
    ):
        if nombre not in self.clientes:
            print(f"No se encontró el cliente '{nombre}'.")
            return False

        if correo:
            self.clientes[nombre]["correo"] = correo
        if telefono:
            self.clientes[nombre]["telefono"] = telefono
        if direccion:
            self.clientes[nombre]["direccion"] = direccion

        self._guardar_datos()
        print(f"Cliente '{nombre}' actualizado correctamente.")
        return True

    def eliminar_cliente(self, nombre):
        if nombre not in self.clientes:
            print(f"No se encontró el cliente '{nombre}'.")
            return False

        del self.clientes[nombre]
        self._guardar_datos()
        print(f"Cliente '{nombre}' eliminado correctamente.")
        return True

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\n--- Lista de clientes ---")
        for nombre, info in self.clientes.items():
            print(f"{info['id']}. {nombre} - {info['correo']}")
