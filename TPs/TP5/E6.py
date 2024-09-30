"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

from typing import List


def pedir_lista() -> List[int]:
    """Añade elementos a una lista hasta que se pare el bucle con -1 y devuelve la lista.

    Pre: No recibe nada.

    Post: Devuelve una lista de enteros.
          si se sale del bucle antes de poner un valor devuelve una lista vacia [].

    """
    lista = []
    while True:
        try:
            n = pedir_num("Ingrese un numero para añadir a la lista (-1 para salir): ")
            if n == -1:
                break
            lista.append(n)
        except ValueError:
            print("Debe ingresar un numero entero.")
    return lista


def pedir_num(msj: str) -> int:
    """Pide un numero al usuario y lo devuelve.

    Pre: msj es un string que se va a mostrar como el mensaje de que va a tener que
         ingresar el usuario.

    Post: Devuelve n un numero entero.

    """
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print("Debe ingresar un numero entero.")
    return n


def buscar_elem(lista: List[int], n: int) -> None:
    """Busca el elemento ingresado en una lista y lo devuelve,
    si no lo encuentra devuelve -1.

    Pre: lista es una lista de enteros.
         n es un numero entero que representa un elemento de la lista.

    Post: Devuelve el indice donde se encuentra n en lista,
          Devuelve -1 si no lo encuentra.

    """
    while True:
        try:
            return lista.index(n)
        except ValueError:
            return -1


def main() -> None:
    """Función principal del programa."""
    lista = pedir_lista()
    contador = 0
    if not lista:
        print("No hay elementos en la lista para buscar.")
    else:
        while True:
            n = pedir_num(
                "Ingrese el valor de un elemento de la lista para saber su indice: "
            )
            index = buscar_elem(lista, n)
            if index == -1:
                contador += 1
                if contador >= 3:
                    break
                print(f"El numero no pertenece a la lista, intento {contador}.")
            else:
                print(f"El numero {n} esta en el indice {index} de la lista.")


if __name__ == "__main__":
    main()
