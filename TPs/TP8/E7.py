"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con-
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""

from typing import Set


def print_set(n: Set[int]) -> None:
    """Prints the set in the terminal.

    Pre: n is a set of integers.

    Post: Prints the set with join for readability and returns None.

    """
    print(" ".join(str(x) for x in n))
    return None


def input_numbers() -> int:
    """Ask the user for input, if its between -1 and 9 (both included), the number is returned.

    Pre: None.

    Post: Returns the number the user gave if it meets the condition, otherwise it asks again.

    """
    while True:
        try:
            n = int(
                input("Ingrese el numero a eliminar de los conjuntos(-1 para salir): ")
            )
            if n >= -1 and n <= 9:
                break
            raise ValueError("El numero debe ser entre 0 y 9.")
        except ValueError as e:
            raise ValueError("Ingrese un numero valido.") from e
    return n


def remove_n(input_number: int, numbers: Set[int]) -> Set[int]:
    """Removes the number specified in the set given.

    Pre: input_number is a integer, the number that will be removed from the set.
         numbers is a set of integers.

    Post: returns the set of integers with the number removed.

    """
    numbers.remove(input_number)
    return numbers


def main() -> None:
    """Main function of the program"""
    numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    while True:
        print_set(numbers)
        try:
            input_n = input_numbers()
            if input_n == -1:
                break
            numbers = remove_n(input_n, numbers)
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Error: El número {input_n} no está en el conjunto.")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
