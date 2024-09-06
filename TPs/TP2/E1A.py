"""
Desarrollar cada una de las siguientes funciones y escribir un programa que
permita verificar su funcionamiento imprimiendo la lista luego de invocar a
cada función:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad
      de elementos también será un número al azar de dos dígitos.
    b. Calcular y devolver el producto de todos los elementos de la lista
       anterior.
    c. Eliminar todas las apariciones de un valor en la lista anterior. El
       valor a eliminar
      se ingresa desde el teclado y la función lo recibe como parámetro. No
      utilizar listas auxiliares.
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin
       usar listas auxiliares. Un ejemplo de lista capicúa es
       [50, 17, 91, 17, 50].
"""

import random as rn


def calc_cantidad_numeros() -> int:
    """Devuelve un numero entero de dos digitos."""
    return rn.randint(10, 99)


def crear_lista(cantidad: int) -> list[int]:
    """Crea la lista y la devuelve.
    Pre -> Recibe un numero entero indicando la cantidad de numeros
      que va a tener la lista.
    Post -> Devuelve la lista creada con numeros enteros aleatorios.
    """
    numeros = [rn.randint(1000, 9999) for _ in range(cantidad)]
    return numeros


def imprimir_datos(cantidad: int, lista: list[int]) -> None:
    """Imprime la lista creada, usando una funcion lambda que formatea
    el texto de una manera mas visual por cada elemento de la lista.
    Pre -> Recibe la cantidad de elementos que tiene la lista en
      un numero entero y la lista de enteros.
    Post -> Imprime la lista con una funcion lambda y la cantidad
      de elementos de la lista.
    """
    imprimir_lista = lambda lista: [print(f"- {e}") for e in lista]
    imprimir_lista(lista)
    print(f"La cantidad de elementos de la lista es de: {cantidad}")
    return None


def main() -> None:
    cantidad = calc_cantidad_numeros()
    lista = crear_lista(cantidad)
    imprimir_datos(cantidad, lista)


if __name__ == "__main__":
    main()
