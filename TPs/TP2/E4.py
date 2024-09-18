"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar
y la lista resultante. La función debe modificar la lista original sin crear
una copia modificada.
"""

import random as rn


def crear_lista(elementos: int) -> list[int]:
    """Crea y devuelve una lista de números enteros aleatorios positivos.

    Pre: Recibe un número entero "elementos" que define la cantidad de números
         en la lista.

    Post: Devuelve una lista de enteros aleatorios, donde cada número está en
          el rango [1, 100].

    """
    # Expresión: for item in iterable
    return [rn.randint(1, 100) for x in range(elementos)]


def eliminar_valores(lista_org: list[int], lista_del: list[int]) -> list[int]:
    """Elimina los valores especificados de la lista original.

    Pre: Recibe dos listas de enteros: "lista_org" (la lista original)
         y "lista_del" (la lista de valores a eliminar).

    Post: Devuelve "lista_org" después de eliminar los valores que estaban en
          "lista_del".
          Los elementos que no estaban en "lista_org" son ignorados.

    """
    for num in lista_del:
        (lambda x, y: x.remove(y) if y in x else None)(lista_org, num)
    return lista_org


def imprimir_lista(lista: list[int], msj: str) -> None:
    """Imprime la lista de números enteros.

    Pre: Recibe una lista de enteros "lista" y un mensaje "msj" para mostrar.

    Post: Imprime el mensaje seguido de los elementos de la lista, separados
          por comas.

    """
    print(msj)
    print(", ".join(map(str, lista)))
    return None


def main() -> None:
    lista_original = crear_lista(20)
    lista_eliminar = crear_lista(20)
    imprimir_lista(lista_original, "Lista original:")
    imprimir_lista(lista_eliminar, "Lista de elementos a eliminar:")
    lista_original = eliminar_valores(lista_original, lista_eliminar)
    imprimir_lista(lista_original, "Lista sin duplicados:")


if __name__ == "__main__":
    main()
