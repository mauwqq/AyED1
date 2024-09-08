"""
Escribir una función que reciba una lista de números enteros como parámetro y
la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las
proporciones relativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por
ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

import random as rn


def crear_lista() -> list[int]:
    """Creo una lista por comprension de 10 valores entre 1 y 10.
    Uso "_" porque el valor de la variable declarada solo la voy a usar para
    eso.
    """
    return [rn.randint(1,10) for _ in range(10)]


def normalizar_lista(lista: list[int]) -> list[float]:
    """Normaliza la lista brindada y la devuelve, para eso divide cada numero
    por la suma total de todos los numeros de la lista.
    Pre -> Recibe una lista de enteros.
    Post -> Devuelve una lista de los elementos normalizados para 0 y 1.
    """
    total = sum(list(lista))
    return list(map(lambda x: x / total ,lista))


def imprimir_lista(lista: list[int], msj: str) -> None:
    print(msj)
    print(" ".join(f"{e:.2f}" for e in lista))


def main() -> None:
    lista = crear_lista()
    lista_norm = normalizar_lista(lista)
    imprimir_lista(lista, f"{"-"*13}lista{"-"*13}")
    imprimir_lista(lista_norm, f"{"-"*7}lista normalizada{"-"*7}")
    print(
          f"{"-"*31}\n",
          "El total de la lista normalizada es de:",
          sum(list(lista_norm)),
    )


if __name__ == '__main__':
    main()
