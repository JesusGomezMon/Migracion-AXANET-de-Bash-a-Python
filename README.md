# Migración AXANET de Bash a Python

Sistema de gestión de clientes migrado de Bash a Python. Utiliza programación orientada a objetos, almacenamiento en JSON y una tabla hash (diccionario) para el acceso rápido a los registros.

## Descripción

AXANET permite realizar operaciones CRUD sobre clientes: crear, buscar, actualizar y eliminar. Los datos se persisten en un archivo JSON y se indexan en memoria mediante un diccionario de Python.

## Instalación

```bash
git clone <url-del-repositorio>
cd axanet-python
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación desde la raíz del proyecto:

```bash
python -m src.app
```

Opciones del menú:

1. Crear cliente
2. Buscar cliente
3. Actualizar cliente
4. Eliminar cliente
5. Listar clientes
0. Salir

## Estructura

```text
axanet-python/
├── src/
│   ├── cliente.py      # Clase Cliente
│   ├── gestor.py       # CRUD y tabla hash
│   └── app.py          # Menú principal
├── data/
│   └── clientes.json   # Persistencia JSON
├── tests/
│   └── test_cliente.py
├── .github/workflows/  # GitHub Actions
├── requirements.txt
└── README.md
```

## Tecnologías utilizadas

- Python 3.12
- JSON
- pytest
- flake8
- Git / GitFlow
- GitHub Actions

## Equipo simulado

| Usuario    | Rol                 |
| ---------- | ------------------- |
| Juan Pérez | Desarrollador       |
| Ana López  | Atención al cliente |

## GitFlow

```text
main
develop
feature/crud-operations
feature/validation
```

## Tests

```bash
pytest
```

## Lint

```bash
flake8 src
```
