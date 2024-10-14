"""
Escribir una función que devuelva la suma de los N primeros números naturales.
"""


def sum_(n: int) -> int:
    """Calculates the sum of the first natural numbers of a number.

    Pre: n is a non-negative integer.

    Post: Returns the sum of the first natural numbers of n.

    Raises: ValueError: if n is negative.

    """
    if n < 0:
        raise ValueError("El numero debe ser positivo.")
    if n == 0:
        return 0
    return n + sum_(n - 1)


def main() -> None:
    """Main function of program"""
    print(sum_(20))
    return None


if __name__ == "__main__":
    main()
