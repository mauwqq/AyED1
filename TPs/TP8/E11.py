"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

from typing import Dict
from tabulate import tabulate

vocals = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]


def input_string() -> str:
    """Ask the user for input of a phrase then returns the phrase.

    Pre: None.

    Post: Returns the user input, a string.

    """
    return input("Ingrese la frase: ")


def count_vocals(word: str) -> None:
    """Counts the vocals of a word with dictionary comprehension.

    Pre: word is a string.

    Post: Returns a dictionary with every vocal as key and the sum of appearances in
          the word as values.

    """
    return {vocal: sum(1 for char in word if char.lower() == vocal) for vocal in vocals}


def count_vocals_phrase(phrase: str) -> Dict[str, int]:
    """Counts the vocals every word in a phrase.

    Pre: phrase is a string.

    Post: Returns a dictionary with the words as keys and the sum of every vocal as
          values.

    """
    words = phrase.split()
    return {word: count_vocals(word) for word in words}


def print_result(phrase_count: Dict[str, int]) -> None:
    """Prints the result of the phrase given.

    Pre: phrase_count is a dictionary of strings as keys and integers as values.

    Post: None.

    """
    table_data = []
    for word, counts in phrase_count.items():
        row = [word] + [counts.get(vocal, 0) for vocal in vocals]
        table_data.append(row)
    headers = ["Palabra"] + vocals
    print(table_data)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    return None


def main() -> None:
    """Main function of program."""
    phrase = input_string()
    if not phrase or phrase.isdigit():
        print("No se ingreso ninguna frase.")
    else:
        phrase_count = count_vocals_phrase(phrase)
        print_result(phrase_count)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
