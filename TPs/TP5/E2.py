"""
Realizar una función que reciba como parámetros dos cadenas de caracteres
conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

from typing import Tuple


def pedir_numeros() -> Tuple[int, int]:
    """Pide dos numeros y los devuelve en tuplas.

    Pre: No recibe nada.

    Post: Devuelve una tupla de dos enteros que el usuario ingreso.

    """
    n1, n2 = (
        input("Ingrese dos numeros reales separados por un espacio: ")
        .strip()
        .split(" ", 1)
    )
    return (n1, n2)


def suma(a: str, b: str) -> int:
    """Suma dos valores que recibe como parametro y los retorna, si se produce
    un error en la suma devuelve -1

    Pre: a es un string.
         b es un string.

    Post: Devuelve la suma de a y b o -1 si da error.

    """
    try:
        return int(a) + int(b)
    except ValueError:
        return -1


def main() -> None:
    """Función principal del programa."""
    while True:
        try:
            n1, n2 = pedir_numeros()
            break
        except ValueError:
            print("Valores invalidos, reintentar.")
            continue
    print(suma(n1, n2))


if __name__ == "__main__":
    main()
