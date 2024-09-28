"""
Crear una lista con los cuadrados de los números entre 1 y N
(ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita
imprimir los últimos 10 valores de la lista.
"""

from typing import List


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(
                input(
                    "Ingrese un número entero positivo: ",
                )
            )
            if n > 0:
                break
            print("El número debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un número entero.")
    return n


def crear_lista(longitud: int) -> List[int]:
    """Crea una lista con la longitud dada.

    Pre: Recibe un número entero "longitud" que define la longitud de la lista.

    Post: Devuelve una lista de enteros desde 1 hasta "longitud", inclusive.

    """
    return list(range(1, longitud + 1))


def cuadrado_lista(lista: List[int]) -> List[int]:
    """Calcula el cuadrado de todos los números en la lista.

    Pre: Recibe una lista de enteros positivos.

    Post: Devuelve una nueva lista con el cuadrado de cada número en la lista original.

    """
    return list(map(lambda x: x * x, lista))


def imprimir_lista(lista: List[int]) -> None:
    """Imprime los últimos 10 números cuadrados de la lista.

    Pre: Recibe una lista de números enteros.

    Post: Imprime los últimos 10 números de la lista formateados.
          Si la lista tiene menos de 10 elementos, imprime todos.

    """
    print("Últimos 10 números cuadrados:")
    print("\n".join([f"{i+1}: {num}" for i, num in enumerate(lista[-10:])]))
    return None


def main() -> None:
    """Función principal del programa."""
    longitud = pedir_numero()
    lista_gen = crear_lista(longitud)
    lista_cuadrado = cuadrado_lista(lista_gen)
    imprimir_lista(lista_cuadrado)
    return None


if __name__ == "__main__":
    main()
