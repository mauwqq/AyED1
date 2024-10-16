"""
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos.
"""


def input_string(msj: str) -> str:
    """Asks the user for string input and returns it.

    Pre: msj is a string.

    Post: Returns the user input as a string.

    """
    return input(msj)


def count_subsequence(main_string, sub_string) -> int:
    """Counts the time a substring appears in a string.
    
    Pre: main_string and sub_string are strings.
    
    Post: Returns the occurrences found between the main and sub string, as an integer.

    Raises: ValueError: if main_string or sub_string are empty.

    """
    if not (main_string and sub_string):
        raise ValueError("Ninguna de las dos cadenas puede ser vacia.")
    main_string = main_string.lower()
    sub_string = sub_string.lower()
    count = 0
    for word in main_string.split():
        if word == sub_string:
            count += 1
    return count


def main() -> None:
    """Función principal del programa."""
    main_string = input_string("Ingrese la cadena: ")
    sub_string = input_string("Ingrese la subcadena a buscar: ")
    try:
        quantity = count_subsequence(main_string, sub_string)
    except ValueError as e:
        print(e)
    else:
        print(f"La subcadena '{sub_string}' se encuentra {quantity} veces en la cadena.")
    return None


if __name__ == "__main__":
    main()
