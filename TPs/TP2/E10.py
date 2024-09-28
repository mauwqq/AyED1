"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
los elementos de la primera que sean impares. El proceso deberá realizarse
utilizando la función filter(). Imprimir las dos listas por pantalla.
"""

import random as rn
from typing import List


def crear_lista() -> List[int]:
    """Crea una lista de números enteros aleatorios.

    Pre: No recibe nada.

    Post: Devuelve una lista de enteros aleatorios, donde la longitud de la
          lista es un número aleatorio entre 1 y 100, y cada número está en el
          rango [1, 100].

    """
    return [rn.randint(1, 100) for _ in range(rn.randint(1, 100))]


def filtrar_lista(lista: List[int]) -> List[int]:
    """Filtra la lista para devolver solo los elementos impares.

    Pre: Recibe una lista de números enteros.

    Post: Devuelve una lista de números enteros que contiene solo los elementos
          impares de la lista original.

    """
    return list(filter((lambda x: x % 2 != 0), lista))


def imprimir_lista(lista: List[int], msj) -> None:
    """Imprime los elementos de la lista con un mensaje dado.

    Pre: Recibe una lista de enteros y un mensaje "msj".

    Post: Imprime el mensaje seguido de los elementos de la lista, separados por
          espacios.

    """
    print(msj)
    print(" ".join(str(e) for e in lista))
    return None


def main() -> None:
    """Función principal del programa."""
    lista = crear_lista()
    lista_filtrada = filtrar_lista(lista)
    imprimir_lista(lista, "Lista original:")
    imprimir_lista(lista_filtrada, "Lista que solo contiene los numeros pares:")
    return None


if __name__ == "__main__":
    main()
