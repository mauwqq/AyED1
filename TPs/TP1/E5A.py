"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
"""


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


def es_oblongo(n: int) -> bool:
    """Determina si un número es un número oblongo.
    Un número oblongo es aquel que puede ser expresado
    como el producto de dos números consecutivos:
    O = n * (n + 1).

    Pre: n es un entero no negativo.

    Post: Retorna True si n es un número oblongo,
          y False en caso contrario.

    """
    return (lambda x: any(x == n * (n + 1) for n in range(1, int(x**0.5) + 2)))(n)


def main() -> None:
    """Función principal del programa."""
    n = pedir_numero("Ingrese un numero entero positivo: ")
    if es_oblongo(n):
        print("El número ingresado es oblongo.")
    else:
        print("El número ingresado no es oblongo.")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
