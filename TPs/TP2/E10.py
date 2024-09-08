"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
los elementos de la primera que sean impares. El proceso deberá realizarse
utilizando la función filter(). Imprimir las dos listas por pantalla.
"""

import random as rn


def crear_lista() -> list[int]:
    return [rn.randint(1, 100) for _ in range(rn.randint(1, 100))]


def filtrar_lista(lista: list[int]) -> list[int]:
    """Recibe una lista y devuelve una lista que solo contiene los elementos
    impares de la recibida. Usando filter con una funcion lambda que comprueba
    si el elemento es par o impar, si es impar lo añade a la nueva lista.
    Pre -> Recibe una lista de numeros enteros.
    Post -> Devuelve una lista de numeros enteros impares.
    """
    return list(filter((lambda x: x % 2 != 0), lista))


def imprimir_lista(lista: list[int], msj) -> None:
    print(msj)
    print(" ".join(str(e) for e in lista))


def main() -> None:
    lista = crear_lista()
    lista_filtrada = filtrar_lista(lista)
    imprimir_lista(lista, "Lista original:")
    imprimir_lista(lista_filtrada, "Lista que solo contiene los numeros pares:")


if __name__ == "__main__":
    main()
