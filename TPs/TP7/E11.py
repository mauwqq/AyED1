"""
Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N.
"""

from typing import List


def min_m(m: List[List[int]], row: int = 0, col: int = 0, min_: int = None) -> int:
    """Searches the smallest element in the matrix given. Recursively.

    Pre: m is a matrix.
         row is a non-negative integer.
         col is a non-negative integer.
         min_ is an integer.

    Post: Returns min_, an integer.

    Raises: ValueError: if m is empty.

    """
    if not m:
        raise ValueError("La matriz esta vacia.")
    if min_ is None:
        min_ = m[0][0]
    if row == len(m):
        return min_
    if col == len(m[row]):
        return min_m(m, row + 1, 0, min_)
    min_ = min(min_, m[row][col])
    return min_m(m, row, col + 1, min_)


def main() -> None:
    """Main function of program"""
    m = [[10, 2, 3], [4, 0, 6], [1, -1, 9]]
    print(min_m(m))
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
