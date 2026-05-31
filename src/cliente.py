class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def to_dict(self):
        return {
            "id": self.id_cliente,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion,
        }
