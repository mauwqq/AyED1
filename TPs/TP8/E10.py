"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

from typing import Dict, Tuple


dict_ = {
    "nombre": "Juan",
    "edad": 30,
    "profesión": "Ingeniero",
    "ciudad": "Madrid",
    "pais": "España",
}
keys_to_delete = ["edad", "ciudad"]


def deletekeys() -> Tuple[Dict[int, int], int]:
    """Removes the keys in keys_to_delete from dict_ and counts how many keys did it delete.

    Pre: None.

    Post: Returns the dict with the keys removed and the count of how many deleted.

    """
    return dict_, sum([dict_.pop(key, None) is not None for key in keys_to_delete])


def main() -> None:
    """Main function of program."""
    dict_, count = deletekeys()
    print(count)
    return None


if __name__ == "__main__":
    main()
