"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con
la cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función.
"""

from typing import Tuple


def pedir_string(msj: str) -> str:
    """Solicita al usuario que ingrese un texto y lo devuelve.

    Pre: Recibe msj, un string.

    Post: Retorna la cadena de texto ingresada por el usuario. Un string.

    """
    return input(msj)


def reemplazar_palabra(cadena: str, reemplazar: str, nueva: str) -> Tuple[str, int]:
    """Reemplaza todas las apariciones de una palabra por otra en una cadena.

    Pre: cadena es la cadena de texto donde se realizará el reemplazo.
         reemplazar es la palabra que se desea reemplazar.
         nueva_palabra es la nueva palabra que reemplazará a la anterior.

    Post: Retorna una tupla con la cadena resultante y el número de reemplazos
          realizados.

    """
    palabras = cadena.split()
    palabras_reemplazadas = [
        nueva if palabra == reemplazar else palabra for palabra in palabras
    ]
    contador_reemplazos = sum(1 for palabra in palabras if palabra == reemplazar)
    cadena_resultante = " ".join(palabras_reemplazadas)
    return cadena_resultante, contador_reemplazos


def main() -> None:
    """Función principal del programa."""
    cadena = pedir_string("Ingrese el texto: ")
    reemplazar = pedir_string("Ingrese la palabra a reemplazar: ")
    nueva = pedir_string("Ingrese la nueva palabra: ")
    resultado, cantidad_reemplazos = reemplazar_palabra(cadena, reemplazar, nueva)
    print("Cadena resultante:", resultado)
    print("Cantidad de reemplazos:", cantidad_reemplazos)
    return None


if __name__ == "__main__":
    main()
