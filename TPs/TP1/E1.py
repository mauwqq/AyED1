"""
Desarrollar una función que reciba tres números enteros positivos y devuelva
el mayor de los tres, sólo si éste es único (es decir el mayor estricto).
Devolver -1 en caso de no haber ninguno. No utilizar operadores lógicos
(and, or, not). Desarrollar también un programa para ingresar los tres
valores, invocar a la función y mostrar el máximo hallado, o un mensaje
informativo si éste no existe.
"""

from functools import reduce
from typing import List


def numeros_input() -> List[int]:
    """Pide y guarda 3 números positivos en una lista.

    Pre: No recibe nada.

    Post: Devuelve una lista que contiene exactamente tres números enteros
          positivos.

    """
    numeros = []
    while len(numeros) < 3:
        try:
            numero = input(f"Ingrese el número {len(numeros)+1}: ")
            if not numero.isdigit():
                raise ValueError()
            if numero > 0:
                numeros.append(numero)
            else:
                raise ValueError()
        except ValueError:
            print("Valor inválido, reintentar.")
            return []
    return numeros


def mayor(numeros: List[int]) -> int:
    """Busca el mayor estricto de los 3 y devuelve el número mayor o -1 si no es
    el mayor estricto.

    Pre: Recibe una lista de enteros con los 3 números mayores a 0.

    Post: Devuelve el mayor estricto si existe, si no devuelve -1.

    """
    n_mayor = reduce(lambda x, y: x if x > y else y, numeros)
    rep = numeros.count(n_mayor) - 1
    return n_mayor if rep == 0 else -1


def imprimir_resultados(resultado: int) -> None:
    """Imprime los resultados obtenidos de los procesos anteriores.

    Pre: Recibe el resultado de mayor(), un número entero.

    Post: Si resultado es distinto a -1 imprime el mayor estricto.

    """
    if resultado != -1:
        print(f"El número mayor ingresado es: {resultado}.")
    else:
        print("No hubo ningún número mayor estricto.")
    return None


def main() -> None:
    """Función principal del programa."""
    numeros = numeros_input()
    resultado = mayor(numeros)
    imprimir_resultados(resultado)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
