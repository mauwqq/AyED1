"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar
y la lista resultante. La función debe modificar la lista original sin crear
una copia modificada.
"""

import random as rn


def crear_lista(elementos: int) -> list[int]:
    """Crea y devuelve una lista de veinte numeros enteros positivos."""
    # Expresion for item in iterable
    return [rn.randint(1, 100) for x in range(elementos)]


def eliminar_valores(lista_org: list[int], lista_del: list[int]) -> list[int]:
    """Recibe la lista original y la lista de valores a eliminar y los elimina
    con una funcion lambda y una iteracion.
    Pre -> Recibe las dos listas de enteros.
    Post -> Devuelve la lista limpia.
    """
    for num in lista_del:
        (lambda x, y: x.remove(y) if y in x else None)(lista_org, num)
    return lista_org


def imprimir_lista(lista: list[int], msj: str) -> None:
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
