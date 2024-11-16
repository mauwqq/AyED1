"""
Realizar una función que devuelva el resto de dos números enteros, utilizando res-
tas sucesivas.
"""


def module(n1: int, n2: int) -> int:
    """Calculates the module of a division recursively.

    Pre: n1 and n2 are non-negative integers.

    Post: Returns the module of the division between n1 and n2.

    Raises: ValueError: if n1 or n2 equals '0', or if n1 or n2 are negative numbers.

    """
    if n1 == 0 or n2 == 0:
        raise ValueError("No se puede dividir por cero.")
    if n1 < 0 or n2 < 0:
        raise ValueError("Los numeros deben ser enteros positivos.")
    if n2 > n1:
        return n1
    if n1 == n2:
        return 0
    return module(n1 - n2, n2)


def main() -> None:
    """Main function of program"""
    try:
        print(module(27, 4))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
