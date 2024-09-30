"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

import math


def pedir_num() -> float:
    """Solicita al usuario el numero de mes que desea buscar en la lista.

    Pre: No recibe nada.

    Post: Retorna un número entero positivo que representa el numero de mes.
          Si el usuario ingresa un valor no válido, vuelve a solicitarlo.

    """
    while True:
        try:
            n = float(input("Ingrese un numero para saber su raiz cuadrada: "))
            break
        except ValueError:
            print("Debe ingresar un numero entero.")
    return n


def get_sqrt(n: float) -> float:
    """Calcula la raiz cuadrada de un numero que se le da como parametro.

    Pre: Recibe n un flotante.

    Post: Devuelve la raiz de n.
          Si no se pudo realizar el calculo devuelve -1.

    """
    try:
        return math.sqrt(n)
    except ValueError:
        return -1


def main() -> None:
    """Función principal del programa."""
    n = pedir_num()
    resultado = get_sqrt(n)
    print(
        f"La raiz cuadrada de {n} es: {resultado:.2f}"
        if resultado != -1
        else f"La raiz de {n} no puede conseguirse porque es un numero negativo."
    )
    return None


if __name__ == "__main__":
    main()
