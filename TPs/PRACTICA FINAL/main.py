from typing import List, Tuple, Dict
import json
from tabulate import tabulate


def mostrar_menu() -> None:
    """ """
    opciones = (
        "Salir",
        "Importar datos",
        "Buscar universidad",
        "Exportar alumnos por Universidad",
        "Estadisticas de total de Mujeres egresadas por universidad",
    )
    for i, op in enumerate(opciones):
        print(f"{i}- {op}")
    return None


def pedir_input(msg: str = "") -> str:
    """ """
    return input(msg).strip()


def validacion(valor, f) -> bool:
    """ """
    return f(valor)


def importar_datos(archivo: str) -> List[str]:
    """ """
    try:
        with open(archivo, "rt", encoding="utf-8-sig") as f:
            data = list()
            linea = f.readline()
            while linea:
                linea = f.readline()
                elemento = tuple(map(lambda x: x.strip(), linea.split(",")))
                if len(elemento) > 3 and elemento[2].startswith("Universidad"):
                    data.append(elemento)
        return data
    except (FileNotFoundError, IsADirectoryError, OSError, PermissionError):
        return []


def buscar_universidad() -> None:
    """ """
    data = importar_datos("mujeres_programadoras.csv")
    if not data:
        print("No hay Universidades regitradas.")
        return None
    keyword = pedir_input("Ingrese el nombre a buscar: ")
    busquedas = tuple(linea for linea in data if keyword.lower() in linea[2].lower())
    if not busquedas:
        print("No hay datos a mostrar")
        return None
    busquedas_clean = tuple(
        " ".join(
            (
                busqueda[0],
                busqueda[2],
                busqueda[5],
                busqueda[19] if busqueda[19] else "0",
            )
        )
        .replace("\\", "")
        .replace("'", "")
        .replace('"', "")
        for busqueda in busquedas
    )
    tabua
    return None


def menu() -> None:
    """ """
    while True:
        mostrar_menu()
        op = pedir_input()
        match op:
            case "0":
                print("Saliendo...")
                break
            case "1":
                data = importar_datos("mujeres_programadoras.csv")
            case "2":
                buscar_universidad()
            case "3":
                pass
            case "4":
                pass
            case _:
                print("Ingrese una opcion valida.")
    return None


def main() -> None:
    """Funcion principal del programa."""
    menu()
    return None


if __name__ == "__main__":
    main()
