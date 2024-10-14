"""
Desarrollar una función que devuelva el producto de dos números enteros por sumas
sucesivas.
"""


def product(n1: int, n2: int) -> int:
    """Calculates the product of two numbers recursively.

    Pre: n1 and n2 are both non-negative integers.

    Post: Returns the product of n1 and n2.

    Raises: ValueError: if n1 or n2 are negative numbers.

    """
    if n2 == 0:
        return 0
    if n1 < 0 or n2 < 0:
        raise ValueError("Los numeros deben ser enteros.")
    return n1 + product(n1, n2 - 1)


def main() -> None:
    """Main function of program"""
    try:
        print(product(5, 10))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
