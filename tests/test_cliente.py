from src.cliente import Cliente


def test_cliente():
    cliente = Cliente(
        1,
        "Juan",
        "juan@gmail.com",
        "9981234567",
        "Cancun",
    )

    assert cliente.nombre == "Juan"
