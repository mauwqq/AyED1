"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

from typing import Dict
from tabulate import tabulate


def gen_dict() -> Dict[int, int]:
    """Generates a dictionary with the values 1 to 20 (both included) where the
    values are the square of the key.

    Pre: None

    Post: Returns a dictionary where both keys and values are integers.

    """
    return {n: n**2 for n in range(1, 21)}


def print_dict(dict_: Dict[int, int]) -> None:
    """Prints the given dictionary with tabulate.

    Pre: dict_ is a dictionary. Both keys and values are integers.

    Post: None.

    """
    print(tabulate(dict_.items(), headers=["Numeros", "Cuadrados"], tablefmt="grid"))
    return None


def main() -> None:
    """Main function of program."""
    dict_ = gen_dict()
    print_dict(dict_)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
