"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic-
cionario. Comprobar el comportamiento de la función mediante un programa apro-
piado.
"""

from typing import List

dictionary = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}


def search_key(value: int) -> List[str]:
    """Searches for a value in a dictionary and returns it.

    Pre: value is a non-negative integer.

    Post: returns a List of strings.
    
    """
    keys = [key for key, v in dictionary.items() if v == value]
    return keys


def input_num() -> int:
    """Requests a number from the user, then cast it to float and returns it.

    Pre: None.

    Post Returns a int.

    Raises: ValueError: if the number cant be casted to float.

    """
    while True:
        try:
            return int(
                input("Ingrese el numero a buscar en los valores del diccionario: ")
            )
        except ValueError:
            print("Por favor ingrese un número válido.")


def main() -> None:
    """Main function of program"""
    value = input_num()
    result = search_key(value)
    if result:
        print(f"Las claves que mapean al valor {value} son: {', '.join(result)}")
    else:
        print(f"No se encontraron claves que mapeen al valor {value}.")
    return None

if __name__ == '__main__':
    main()
