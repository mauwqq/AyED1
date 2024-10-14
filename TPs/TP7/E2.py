"""
Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal.
"""


def binary_to_decimal(n: int, power: int = 0) -> int:
    """Calculates the conversion from binary to decimal.

    Pre: n must be a binary number.
         power is an integer number, values 0 by default.

    Post: Returns the decimal value of the binary given, in an integer.

    Raises: ValueError: if n is not a binary number.

    """
    if any(x not in ["1", "0"] for x in str(n)):
        raise ValueError("El numero debe ser binario.")
    if n == 0:
        return 0
    return (n % 10) * (2**power) + binary_to_decimal(n // 10, power + 1)


def main() -> None:
    """Main function of program"""
    try:
        print(binary_to_decimal(101100101))
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
