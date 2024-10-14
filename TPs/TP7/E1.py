"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""


def digits(n: int) -> int:
    """Recursively calculates the quantity of digits a number has.

    Pre: n is a non-negative integer.

    Post: Returns the number of digits in the integer n.

    Raises: ValueError: if n is negative.

    """
    if n < 0:
        raise ValueError("El numero debe ser entero.")
    if n == 0 or n < 10:
        return 1
    return 1 + digits(n // 10)


def main() -> None:
    """Main function of program"""
    try:
        print(digits(10))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
