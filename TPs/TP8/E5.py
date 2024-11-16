"""
En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi-
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función.
"""

from typing import Tuple
import random as rn


def gen_vector() -> Tuple[int, int]:
    """Generates a tuple of two random integers from 1-100.

    Pre: None.

    Post: Returns a tuple of two random generated integers.

    """
    return (rn.randint(1, 100), rn.randint(1, 100))


def check_orthogonal(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    """Checks if the two vectors given are orthogonal.

    Pre: v1 and v2 are tuples of integers representing vectors.

    Post: True if the vectors are orthogonal(their dot product is 0),
          otherwise False.

    """
    return (v1[0] * v2[0]) + (v1[1] * v2[1]) == 0


def main() -> None:
    """Main function of program"""
    v1, v2 = gen_vector(), gen_vector()
    print(
        f"{v1}, {v2}: Son ortogonales."
        if check_orthogonal(v1, v2)
        else f"{v1}, {v2}: No son ortogonales."
    )
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
