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
    print("Ingrese un numero entre el 1 y el 100")
    while True:
        try:
            n = int(
                input(
                    "Inserte la cantidad de numeros aleatorios a generar: ",
                )
            )
            if n > 0 and n <= 100:
                break
            print(
                "El numero debe estar entre el 1 y el 100 inclusives.",
            )
        except ValueError:
            print("Debe ingresar un numero entero.")
    return n


def generar_lista(numero: int) -> list[int]:
    """Genera y retorna una lista de numeros entre 1-100 con la longitud
    que el usuario ingreso.
    Pre -> Recibe un numero entero que define la longitud de la lista.
    Post -> Genera los numeros en la lista y la devuelve.
    """
    return [rn.randint(1, 100) for _ in range(numero)]


def comprobar_duplicado(numeros: list[int]) -> bool:
    """Comprueba si hay numeros duplicados en la lista generada y retorna
    un booleano.
    Pre -> Recibe la lista de enteros generada.
    Post -> Crea un conjunto para eliminar duplicados y comprueba la
        longitud de el set(como lista) con la lista original."""
    numeros_set = [(set(numeros))]
    return len(numeros) != len(numeros_set)


def eliminar_duplicados(numeros: list[int]) -> list[int]:
    """Elimina los duplicados si los hay y devuelve la lista sin ellos.
    Pre -> Recibe la lista de enteros generada.
    Post -> Devuelve una lista creada a partir de un set, sin duplicados.
    """
    return [set(numeros)]


def main() -> None:
    cantidad = pedir_numero()
    numeros = generar_lista(cantidad)
    duplicado = comprobar_duplicado(numeros)
    lista_sin_duplicados = eliminar_duplicados(numeros)


if __name__ == "__main__":
    main()
