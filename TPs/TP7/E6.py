"""
La función de Ackermann A(m,n) se define de la siguiente forma:
n+1                 si m = 0
A(m-1,1)            si n = 0
A(m-1,A(m,n-1))     de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de
m entre 0 y 3 y de n entre 0 y 7.
"""

from typing import List, Optional
from tabulate import tabulate


def a(m: int, n: int) -> int:
    """Calculates the Ackermann function.

    Pre: m and n are non-negative integers.

    Post: Returns the result of a(m, n) where a is the Ackermann function.

    Raises: ValueError: if m or n are less than cero.

    """
    if m < 0 or n < 0:
        raise ValueError("The numbers must be positive.")
    if m == 0:
        return n + 1
    if n == 0:
        return a(m - 1, 1)
    return a(m - 1, a(m, n - 1))


def get_values() -> List[List[Optional[int]]]:
    """Generates a list by comprehension with all the cases of m between 0 and 3,
    and n between 0 and 7.

    Pre: None.

    Post: Returns a matrix.

    """
    return [
        [n] + [a(m, n) if not (m == 3 and n >= 7) else "RecErr" for m in range(4)]
        for n in range(8)
    ]


def print_table() -> None:
    """Prints the values with tabulate.

    Pre: None.

    Post: None.

    """
    headers = ["n\\m"] + [f"{m}" for m in range(4)]
    values = get_values()
    print(tabulate(values, headers=headers, tablefmt="grid"))
    return None


def main() -> None:
    """Main function of program"""
    print_table()
    return None


if __name__ == "__main__":
    main()
