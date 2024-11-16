"""
Intercalar los elementos de una lista entre los elementos de otra. La
intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas
y no se creará una lista nueva sino que se modificará la primera. Por ejemplo,
si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como
[8, 5, 1, 9, 3, 7]. Las listas pueden tener distintas longitudes.
"""

import random as rn
from typing import List


def crear_lista() -> List[int]:
    """Crea una lista de números aleatorios entre 1 y 10.

    Pre: No recibe nada.

    Post: Devuelve una lista de enteros aleatorios,
          la longitud de la lista es un número aleatorio entre 5 y 10,
          y cada número está en el rango [1, 10].

    """
    return [rn.randint(1, 10) for _ in range(rn.randint(5, 10))]


def mezclar_listas(lista1: List[int], lista2: List[int]) -> None:
    """Mezcla las listas usando slicing, itera la longitud de la menor lista,
    usando min(). Cuando start:stop son iguales en el slicing, es como una
    posición de inserción. En realidad estoy insertado una lista adentro de
    lista1, por eso tengo que pasar el valor de lista2 como: [lista2[i]],
    tiene que ser un iterable, a su vez:
        i = 0 -> 2 * 0 + 1 = 1
        i = 1 -> 2 * 1 + 1 = 2
        i = 2 -> 2 * 2 + 1 = 5
    Extend añade los números restante si la lista2 es más larga que la 1.

    Pre: Recibe dos listas de enteros.

    Post: Modifica "lista1" para incluir los elementos de "lista2" intercalados.
          Si "lista2" es más larga, los elementos restantes se añaden al final
          de "lista1".
    """
    long = min(len(lista1), len(lista2))
    extend = len(lista2) > len(lista1)
    for i in range(long):
        lista1[2 * i + 1 : 2 * i + 1] = [lista2[i]]
    if extend:
        lista1.extend(lista2[long:])
    return None


def imprimir_lista(lista: List[int], msj: str) -> None:
    """Imprime los elementos de la lista con un mensaje dado.

    Pre: Recibe una lista de enteros y un string msj.

    Post: Imprime el mensaje seguido de los elementos de la lista.

    """
    print(msj)
    print(" ".join(str(e) for e in lista))
    return None


def main():
    """Función principal del programa."""
    lista1 = crear_lista()
    imprimir_lista(lista1, "Primera lista:")
    lista2 = crear_lista()
    imprimir_lista(lista2, "Segunda lista:")
    mezclar_listas(lista1, lista2)
    imprimir_lista(lista1, "Lista intercalada:")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
