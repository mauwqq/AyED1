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


def producto_lista(lista: list[int]) -> int:
    """Retorna el producto de una lista usando lambda y reduce.
    Pre -> Recibe una lista de enteros.
    Post -> Usando reduce aplico una funcion lambda que 
        multiplica los dos valores que agarra y los devuelve,
        reduce hace que se le aplique secuencialmente a cada
        elemento de la lista.
    """
    return reduce(lambda a, b: a * b, lista)


def pedir_numero() -> int:
    while True:
        try:
            n = int(input("Ingrese el numero que desee sacar de la lista: "))
            if n > 0:
                break
            print("El numero debe ser positivo.")
        except ValueError:
            print("Se debe ingresar un numero.")
    return n


def eliminar_valor_lista(numero, lista) -> None:
    while True:
        try:
            lista.remove(numero)
            print("Numero eliminado...")
        except ValueError:
            print("No se encontro el numero en la lista.")
            break


def es_capicua(lista: list[int]) -> bool:
    """Recibe una lista y comprueba si es capicua o no.
    Pre -> Recibe una lista de enteros.
    Post -> Recordando que lista[start:stop:step], cuando indicamos [::-1],
        el :: no marca start ni stop por lo que abarca toda la lista. Mientras
        que el -1 indica que debe hacerse el slicing en sentido contrario.
    """
    return lista[::-1] == lista


def main() -> None:
    cantidad = calc_cantidad_numeros()
    lista = crear_lista(cantidad)
    producto = producto_lista(lista)
    numero = pedir_numero()
    #eliminar_valor_lista(numero, lista)
    #print(es_capicua(crear_lista(10)))
    #es_capicua(lista=[50, 17, 91, 17, 50])

if __name__ == "__main__":
    main()

