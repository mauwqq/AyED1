"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

from typing import Tuple
import random as rn


def gen_domino_card() -> Tuple[int, int]:
    """Generates one tuple with two integers between 0-6 representing the domino
    cards.

    Pre: None.

    Post: Returns a tuple of two integers.

    """
    return (rn.randint(0, 6), rn.randint(0, 6))


def match_dominoes(d1: Tuple[int, int], d2: Tuple[int, int]) -> bool:
    """Checks if the two dominoes matches.The "&" operator
    (a shortcut to intersection()) returns a set containing only the items that
    exists in both sets.

    Pre: d1 and d2 are tuples with two integers.

    Post: Parsing it to a boolean to return True/False.
          Returns True if the intersection has values.
          Returns False if the intersection is empty.

    """
    return bool(set((d1)) & set((d2)))


def main() -> None:
    """Main function of the program"""
    d1, d2 = gen_domino_card(), gen_domino_card()
    # print(d1, d2)
    # print(match_dominoes(d1,d2))
    if match_dominoes(d1, d2):
        print(f"Las fichas de domino: {d1} / {d2} encajan.")
    else:
        print(f"Las fichas de domino: {d1} / {d2} no encajan.")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
