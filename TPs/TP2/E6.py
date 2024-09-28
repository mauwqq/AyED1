"""
Escribir una función que reciba una lista de números enteros como parámetro y
la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las
proporciones relativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por
ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

import random as rn
from typing import List


def crear_lista() -> List[int]:
    """Crea una lista de 10 valores aleatorios entre 1 y 10.

    Pre: No recibe nada.

    Post: Devuelve una lista de 10 enteros aleatorios, donde cada número está
          en el rango [1, 10].
    
    """
    return [rn.randint(1,10) for _ in range(10)]


def normalizar_lista(lista: List[int]) -> List[float]:
    """Normaliza la lista proporcionada.

    Pre: Recibe una lista de enteros. La suma de los elementos debe ser 1.
 
    Post: Devuelve una lista de números flotantes, donde cada elemento es el
          resultado de dividir cada número de la lista original por la suma
          total de todos los números.

    """
    total = sum(list(lista))
    return list(map(lambda x: x / total,lista))


def imprimir_lista(lista: List[int], msj: str) -> None:
    """Imprime los elementos de la lista con un mensaje dado.

    Pre: Recibe una lista de números flotantes y un mensaje "msj".

    Post: Imprime el mensaje seguido de los elementos de la lista,
          formateados a dos decimales.

    """
    print(msj)
    print(" ".join(f"{e:.2f}" for e in lista))
    return None


def main() -> None:
    """Función principal del programa."""
    lista = crear_lista()
    lista_norm = normalizar_lista(lista)
    imprimir_lista(lista, f"{"-"*13}lista{"-"*13}")
    imprimir_lista(lista_norm, f"{"-"*7}lista normalizada{"-"*7}")
    print(
          f"{"-"*31}\n",
          "El total de la lista normalizada es de:",
          sum(list(lista_norm)),
    )
    return None


if __name__ == '__main__':
    main()
