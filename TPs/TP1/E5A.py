"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
"""


def pedir_num() -> int:
    """Solicita un número entero positivo al usuario y lo retorna.

    Pre: No recibe nada.

    Post: Si el numero ingresado es un entero positivo devuelve el numero, de no
          ser asi, se repite el bucle hasta que se cumpla la condicion.

    """
    while True:
        try:
            n = int(input("Ingrese el número a comprobar: "))
            if n > 0:
                return n
            print("El número debe ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")


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
    n = pedir_num()
    if es_oblongo(n):
        print("El número ingresado es oblongo.")
    else:
        print("El número ingresado no es oblongo.")
    return None


if __name__ == "__main__":
    main()
