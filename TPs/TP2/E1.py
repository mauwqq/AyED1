"""
Desarrollar cada una de las siguientes funciones y escribir un programa que
permita verificar su funcionamiento imprimiendo la lista luego de invocar a
cada función:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad
      de elementos también será un número al azar de dos dígitos.
    b. Calcular y devolver el producto de todos los elementos de la lista
       anterior.
    c. Eliminar todas las apariciones de un valor en la lista anterior. El
       valor a eliminar se ingresa desde el teclado y la función lo recibe
       como parámetro. No utilizar listas auxiliares.
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin
       usar listas auxiliares. Un ejemplo de lista capicúa es
       [50, 17, 91, 17, 50].
"""

from functools import reduce
import random as rn


def calc_cantidad_numeros() -> int:
    """Devuelve un número entero de dos dígitos.

    Post: Devuelve un número entero aleatorio entre 10 y 99 (ambos inclusive).

    """
    return rn.randint(10, 99)


def crear_lista(cantidad: int) -> list[int]:
    """Crea y devuelve una lista de números enteros aleatorios.

    Pre: Recibe un número entero "cantidad" que indica la cantidad de números
         que tendrá la lista. "cantidad" debe ser positivo.

    Post: Devuelve una lista de enteros aleatorios de 4 dígitos (entre 1000 y 9999),
          con una longitud igual a "cantidad".

    """
    return [rn.randint(1000, 9999) for _ in range(cantidad)]


def producto_lista(lista: list[int]) -> int:
    """Retorna el producto de los elementos de una lista.

    Pre: Recibe una lista de enteros no vacía.

    Post: Devuelve el resultado de multiplicar todos los elementos de la lista.

    """
    return reduce(lambda a, b: a * b, lista)


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese el número que desee sacar de la lista: "))
            if n > 0:
                break
            print("El número debe ser positivo.")
        except ValueError:
            print("Se debe ingresar un número.")
    return n


def eliminar_valor_lista(numero: int, lista: list[int]) -> list[int]:
    """Elimina todas las ocurrencias del número especificado de la lista.

    Pre: Recibe un número entero "numero" y una lista de enteros "lista".

    Post: Devuelve la lista con todas las ocurrencias de "numero" eliminadas.
          Si el número no está en la lista, la lista permanece sin cambios.

    """
    while True:
        try:
            lista.remove(numero)
            print("Número eliminado...")
        except ValueError:
            print("No se encontró el número en la lista.")
            break
    return lista


def es_capicua(lista: list[int]) -> bool:
    """Verifica si la lista es capicua (palíndromo).

    Pre: Recibe una lista de enteros no vacía.

    Post: Devuelve "True" si la lista es capicua (es decir, si se lee igual
          de izquierda a derecha que de derecha a izquierda); si no,  devuelve
          "False".

    """
    return lista[::-1] == lista


def main() -> None:
    cantidad = calc_cantidad_numeros()
    lista = crear_lista(cantidad)
    producto = producto_lista(lista)
    numero = pedir_numero()


if __name__ == "__main__":
    main()
