"""
Escribir una función que sume todos los elementos de una matriz de M x N y de-
vuelva el resultado. No usar la función sum().
"""

from typing import List


def sum_matrix(m: List[List[int]], row: int = 0, col: int = 0) -> int:
    """Sums the matrix given, recursively.

    Pre: m is a matrix, a list of lists with integers.
         row is a non-negative integer, values 0 by default.
         col is a non-negative integer, values 0 by default.

    Post: Returns the sum of the matrix, an integer.

    Raises: ValueError: if m is empty.

    """
    if not m:
        raise ValueError("La matriz esta vacia.")
    if row == len(m):
        return 0
    if col == len(m[row]):
        return sum_matrix(m, row + 1, 0)
    return m[row][col] + sum_matrix(m, row, col + 1)


def main() -> None:
    """Main function of program"""
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        print(sum_matrix(m))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
