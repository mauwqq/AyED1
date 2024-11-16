"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

from typing import Dict
from tabulate import tabulate


def input_number() -> int:
    """Ask the user for input, if the number is above 0 the number is returned.

    Pre: None.

    Post: Returns the number the user gave if it meets the condition, otherwise it asks again.

    """
    while True:
        try:
            n = int(input("Ingrese el numero: "))
            if n > 0:
                break
            raise ValueError("El numero debe ser mayor a cero.")
        except ValueError as e:
            raise ValueError("Ingrese un numero valido.") from e
    return n


def multiplication_table(n: int) -> Dict[int, int]:
    """Returns a dictionary with n multiplication table, from 1 to 12 (both included)

    Pre: n is a integer.

    Post: Returns a dictionary of integers.

    """
    return {x: n * x for x in range(1, 13)}


def print_dict(dict_: Dict[int, int]) -> None:
    """Prints the given dictionary with tabulate.

    Pre: dict_ is a dictionary. Both keys and values are integers.

    Post: None.

    """
    print(tabulate(dict_.items(), tablefmt="grid"))
    return None


def main() -> None:
    """Main function of program."""
    n = input_number()
    dict_ = multiplication_table(n)
    print_dict(dict_)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
