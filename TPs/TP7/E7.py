"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Má-
ximo Común Divisor (también llamado Divisor Común Mayor) basándose en las si-
guientes propiedades:
MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y  => MCD(X, Y) = MCD(X–Y, Y).
Utilizando la función anterior calcular el MCD de todos los elementos de una lista de
números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
utilizar iteraciones en ninguna etapa del proceso.
"""

from typing import List


def mcd(x: int, y: int) -> int:
    """Calculates the MCD of two or three numbers. Recursively.

    Pre: x and y are non-negative integers.

    Post: Returns the mcd of x, y. An integer.

    Raises: ValueError: if x or y are negative numbers.

    """
    if x < 0 or y < 0:
        raise ValueError("Los numeros deben ser positivos.")
    if x == y:
        return x
    if x > y:
        return mcd(x - y, y)
    return mcd(x, y - x)


def mcd_list(n: List[int]) -> int:
    """Parses the list given to the mcd function.

    Pre: n is a list of integers.

    Post: Returns the mcd of the list given.

    Raises: ValueError: if n is an empy list.

    """
    if not n:
        raise ValueError("La lista no puede estar vacía.")
    if len(n) == 1:
        return n[0]
    return mcd(mcd(n[0], n[1]), mcd_list(n[2:])) if len(n) > 2 else mcd(n[0], n[1])


def main() -> None:
    """Main function of program"""
    n_list = [7, 5, 14]
    result = mcd_list(n_list)
    print(f"El MCD de {n_list} es: {result}")
    return None


if __name__ == "__main__":
    main()
