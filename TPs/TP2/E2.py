"""
Escribir funciones para:
    a. Generar una lista de N números aleatorios del 1 al 100. El valor de N
    se ingresa a través del teclado.
    b. Recibir una lista como parámetro y devolver True si la misma contiene
    algún elemento repetido. La función no debe modificar la lista.
    c. Recibir una lista como parámetro y devolver una nueva lista con los
    elementos únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""

import random as rn
from typing import List


def pedir_numero(msj: str) -> int:
    """Solicita al usuario la cantidad de caracteres que se desean extraer.

    Pre: Recibe una cadena de caracteres de tipo string.

    Post: Retorna un número entero positivo que representa la cantidad de caracteres.
          Si el usuario ingresa un valor no válido, vuelve a solicitarlo.

    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero positivo.")
    return n


def generar_lista(numero: int) -> List[int]:
    """Genera y retorna una lista de números aleatorios entre 1 y 100.

    Pre: Recibe un número entero "numero" que define la longitud de la lista.

    Post: Devuelve una lista de enteros aleatorios, con una longitud igual a "numero",
          donde cada número está en el rango [1, 100].

    """
    return [rn.randint(1, 100) for _ in range(numero)]


def comprobar_duplicado(numeros: List[int]) -> bool:
    """Comprueba si hay números duplicados en la lista.

    Pre: Recibe una lista de enteros positivos generada.

    Post: Devuelve "True" si hay duplicados en la lista, si no devuelve "False".

    """
    numeros_set = [(set(numeros))]
    return len(numeros) != len(numeros_set)


def eliminar_duplicados(numeros: List[int]) -> List[int]:
    """Elimina los duplicados de la lista y devuelve la lista sin ellos.

    Pre: Recibe la lista de enteros generada.

    Post: Devuelve una lista de enteros que contiene solo los valores únicos
          de la lista original, eliminando los duplicados.

    """
    return list(set(numeros))


def main() -> None:
    """Función principal del programa."""
    cantidad = pedir_numero("Ingrese la cantidad de numeros aleatorios a generar: ")
    numeros = generar_lista(cantidad)
    if comprobar_duplicado(numeros):
        lista_sin_duplicados = eliminar_duplicados(numeros)
    else:
        lista_sin_duplicados = numeros.copy()
    print("Lista original:", " ".join(str(n) for n in numeros))
    print("Lista sin duplicados:", " ".join(str(n) for n in lista_sin_duplicados))
    return None


if __name__ == "__main__":
    main()
