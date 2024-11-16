"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""

from typing import Set, List


def get_input() -> str:
    """Asks the user for input and returns it.

    Pre: None.

    Post: Returns a string containing the user input, without symbols.

    """
    return "".join(
        " " if char in [".", ",", "!", "?", ":", ";"] else char
        for char in input("Ingrese el texto que quiere modificar: ")
    )


def remove_dupes(text: str) -> Set[str]:
    """Removes duplicated words in the text given.

    Pre: text is a string of characters.

    Post: Returns a set splitted by " " of words, removing the duplicates.

    """
    return set(text.split())


def organize_lengh(words: Set[str]) -> List[str]:
    """Sorts the words given in a Set.

    Pre: words is a Set of strings.

    Post: Returns a list of the words given sorted by lengh from high to low.

    """
    return sorted(words, key=len, reverse=True)


def main() -> None:
    """Main function of program"""
    text = get_input()
    words = remove_dupes(text)
    org_words = organize_lengh(words)
    print("\n".join(org_words))
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
