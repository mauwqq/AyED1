"""
Utilizar la técnica de listas por comprensión para construir una lista con todos
los números impares comprendidos entre 100 y 200.
"""

from typing import List


def crear_lista() -> List[int]:
    """Crea una lista de números impares entre 100 y 200.

    Pre: No recibe nada.

    Post: Devuelve una lista de enteros que contiene todos los números impares
          en el rango [100, 200].

    """
    return [e for e in range(100, 201) if e % 2 != 0]


def imprimir_lista(lista: List[int]) -> None:
    """Imprime los elementos de la lista.

    Pre: Recibe una lista de enteros.

    Post: Imprime los elementos de la lista, separados por espacios.

    """
    print(" ".join(str(e) for e in lista))
    return None


def main():
    """Función principal del programa."""
    lista = crear_lista()
    imprimir_lista(lista)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
