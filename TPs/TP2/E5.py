"""
Escribir una función que reciba una lista como parámetro y devuelva True si la
lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
Desarrollar además un programa para verificar el comportamiento de la función.
"""

import random as rn
from typing import List


def crear_lista(elementos: int) -> List[int]:
    """Crea una lista de números enteros aleatorios positivos.

    Pre: Recibe un número entero "elementos" que indica la longitud de la lista.

    Post: Devuelve una lista de enteros aleatorios, donde cada número está en
          el rango [1, 111], con una longitud igual a "elementos".

    """
    return [rn.randint(1, 111) for _ in range(elementos)]


def verif_lista_ordenada(lista: List[int]) -> bool:
    """Verifica si la lista está ordenada en orden ascendente.

    Pre: Recibe una lista de enteros.

    Post: Devuelve "True" si la lista está ordenada, sino, devuelve "False".

    """
    return lista == sorted(lista)


def main() -> None:
    """Función principal del programa."""
    lista = crear_lista(10)
    lista_ordenada = [1, 2, 3]
    lista_desordenada = ["b", "a"]
    print(
        " ".join(str(e) for e in lista),
        f": {verif_lista_ordenada(lista)}",
    )
    print(
        " ".join(str(e) for e in lista_ordenada),
        f": {verif_lista_ordenada(lista_ordenada)}",
    )
    print(
        " ".join(str(e) for e in lista_desordenada),
        f": {verif_lista_ordenada(lista_desordenada)}",
    )
    return None


if __name__ == "__main__":
    main()
