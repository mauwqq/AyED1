"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar
funciones que generen cada una de ellas sin intervención humana y escribir un
programa que las invoque e imprima por pantalla. El tamaño de las matrices debe
establecerse como N x N, donde N se ingresa a través del teclado.
"""

from tabulate import tabulate
from typing import List


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese el tamaño de la matriz: "))
            if n > 0:
                break
            print("El número tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def f_a(n: int) -> List[List[int]]:
    """Genera una matriz de tamaño n x n donde los elementos de la diagonal son
    números impares.

    Pre: n es un entero que define el tamaño de la matriz.

    Post: Retorna una lista de listas (matriz) donde el elemento en la posición
          (i, i) es (2 * i + 1) y todos los demás elementos son 0.

    """
    return [[i * 2 + 1 if i == j else 0 for j in range(n)] for i in range(n)]


def f_b(n: int) -> List[List[int]]:
    """Genera una matriz de tamaño n x n con un patrón específico basado entero
    potencias de 3.

    Pre: n es un entero que define el tamaño de la matriz.

    Post: Retorna una lista de listas (matriz) donde el elemento en la posición
          (i, 3 - i) es 27 dividido por 3 elevado a la i, y todos los demás
          elementos son 0.

    """
    return [[27 // (3**i) if j == 3 - i else 0 for j in range(n)] for i in range(n)]


def f_c(n: int) -> List[List[int]]:
    """Genera una matriz de tamaño n x n con un patrón decreciente en cada fila.

    Pre: n es un entero que define el tamaño de la matriz.

    Post: Retorna una lista de listas (matriz) donde el elemento en la posición
          (i, j) es (4 - i) si j es menor o igual a i, y 0 en caso contrario.

    """
    return [[4 - i if j <= i else 0 for j in range(n)] for i in range(n)]


def f_d(n: int) -> List[List[int]]:
    """Genera una matriz de tamaño n x n con potencias de 2 en cada fila.

    Pre: n es un entero que define el tamaño de la matriz.

    Post: Retorna una lista de listas (matriz) donde cada fila tiene el mismo
          valor, que es 2 elevado a (3 - i) para cada i, y todos los elementos
          en la fila son iguales.

    """
    return [[2 ** (3 - i) for j in range(n)] for i in range(n)]


def f_e(n: int) -> List[List[int]]:
    """Genera una matriz de tamaño n x n con un patrón alternante de números.
    PD: valor := valor + 1 asigna el valor de (valor + 1) a valor y a su vez
    evalua la expresion. Se incrementa valor y a su vez se usa.

    Pre: n es un entero que define el tamaño de la matriz.

    Post: Retorna una lista de listas (matriz) donde los elementos en posiciones
          donde la suma de los índices es impar se incrementan secuencialmente,
          y 0 en caso contrario.

    """
    valor = 0
    return [
        [(valor := valor + 1) if (i + j) % 2 == 1 else 0 for j in range(n)]
        for i in range(n)
    ]


def main() -> None:
    """Función principal del programa."""
    n = pedir_numero()
    print(tabulate(f_a(n)))
    print(tabulate(f_b(n)))
    print(tabulate(f_c(n)))
    print(tabulate(f_d(n)))
    print(tabulate(f_e(n)))
    return None


if __name__ == "__main__":
    main()
