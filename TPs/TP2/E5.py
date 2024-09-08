"""
Escribir una función que reciba una lista como parámetro y devuelva True si la
lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
Desarrollar además un programa para verificar el comportamiento de la función.
"""

import random as rn


def crear_lista(elementos: int) -> list[int]:
    """Crea una lista usando listas por comprension, del rango que se le dio a
    la funcion.
    Pre -> Recibe un numero entero que indica la longitud de la lista.
    Post -> Retorno la lista por comprension de la longitud dada.
    """
    return [rn.randint(1, 111) for _ in range(elementos)]


def verif_lista_ordenada(lista: list[int]) -> bool:
    return lista == sorted(lista)


def main() -> None:
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


if __name__ == "__main__":
    main()
