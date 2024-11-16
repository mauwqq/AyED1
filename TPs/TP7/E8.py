"""
Realizar la implementación recursiva del método de selección para ordenar una lista
de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las
funciones min() ni max() de Python.
"""

from typing import List


def order(n: List[int], start: int = 0) -> List[int]:
    """Sorts a list in ascending order using recursivity.

    Pre: n is a list of integers.
         start is non-negative integer, values 0 by default.

    Post: Returns the list sorted in ascending order.

    Raises: ValueError: if n is empty.

    """
    if not n:
        raise ValueError("La lista esta vacia.")
    if start == len(n) - 1:
        return n
    min_i = start
    for i, elem in enumerate(n[start + 1 :], start=start + 1):
        if elem < n[min_i]:
            min_i = i
    n[start], n[min_i] = n[min_i], n[start]
    return order(n, start + 1)


def main() -> None:
    """Main function of program"""
    n = [25, 1, 23, 45, 23, 5, 6, 7, 45, 3, 1, 2]
    try:
        print(order(n))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
