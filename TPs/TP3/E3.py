"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N 2), de tal forma que ningún número se
repita. Imprimir la matriz por pantalla.
"""

import random as rn


def generar_matriz(n: int) -> list[list[int]]:
    """Genera una matriz de N x N con números enteros únicos aleatorios en el
    intervalo [0, N^2).

    Pre: n es un entero positivo que representa el tamaño de la matriz.

    Post: Retorna una matriz de tamaño N x N llena de números únicos aleatorios.

    """
    numeros = rn.sample(range(n * n), n * n)
    matriz = []
    for i in range(n):
        fila = numeros[i * n : (i + 1) * n]
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """Imprime la matriz en formato legible.

    Pre: matriz es una lista de listas que representa una matriz.

    Post: Imprime la matriz en la consola.

    """
    for fila in matriz:
        print(" ".join(map(str, fila)))
    print()


def main() -> None:
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz = generar_matriz(n)
    print("Matriz generada:")
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()