"""
Realizar una función recursiva para imprimir una matriz de M x N con el formato
apropiado.
"""

from typing import List


def print_matrix(m: List[List[int]], start: int = 0) -> None:
    if start == len(m):
        return None
    print(" ".join(str(n) for n in m[start]))
    return print_matrix(m, start + 1)


def main() -> None:
    """Main function of program"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    return None


if __name__ == "__main__":
    main()
