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


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    print("Ingrese un número entre el 1 y el 100")
    while True:
        try:
            n = int(
                input(
                    "Inserte la cantidad de números aleatorios a generar: ",
                )
            )
            if n > 0 and n <= 100:
                break
            print(
                "El número debe estar entre el 1 y el 100 inclusive.",
            )
        except ValueError:
            print("Debe ingresar un número entero.")
    return n


def generar_lista(numero: int) -> list[int]:
    """Genera y retorna una lista de números aleatorios entre 1 y 100.

    Pre: Recibe un número entero "numero" que define la longitud de la lista.

    Post: Devuelve una lista de enteros aleatorios, con una longitud igual a "numero",
          donde cada número está en el rango [1, 100].

    """
    return [rn.randint(1, 100) for _ in range(numero)]


def comprobar_duplicado(numeros: list[int]) -> bool:
    """Comprueba si hay números duplicados en la lista.

    Pre: Recibe una lista de enteros positivos generada.

    Post: Devuelve "True" si hay duplicados en la lista, si no devuelve "False".

    """
    numeros_set = [(set(numeros))]
    return len(numeros) != len(numeros_set)


def eliminar_duplicados(numeros: list[int]) -> list[int]:
    """Elimina los duplicados de la lista y devuelve la lista sin ellos.

    Pre: Recibe la lista de enteros generada.

    Post: Devuelve una lista de enteros que contiene solo los valores únicos
          de la lista original, eliminando los duplicados.

    """
    return [set(numeros)]


def main() -> None:
    cantidad = pedir_numero()
    numeros = generar_lista(cantidad)
    duplicado = comprobar_duplicado(numeros)
    lista_sin_duplicados = eliminar_duplicados(numeros)


if __name__ == "__main__":
    main()
