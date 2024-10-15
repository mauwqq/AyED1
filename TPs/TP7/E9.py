"""
Realizar una función recursiva para imprimir una matriz de M x N con el formato
apropiado.
"""

from typing import List


def print_matrix(m: List[List[int]], start: int = 0) -> None:
    """Recursively prints the matrix given.

    Pre: m is a matrix, a list of lists with integers.
         start is a non-negative integer, values 0 by default.

    Post: None.

    Raises: ValueError: if m is empty.

    """
    if not m:
        raise ValueError("La matriz esta vacia.")
    if start == len(m):
        return None
    print(" ".join(str(n) for n in m[start]))
    return print_matrix(m, start + 1)


def main() -> None:
    """Main function of program"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        print_matrix(matrix)
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
