"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
"""


def pedir_num() -> int:
    """Solicita un número entero positivo al usuario y lo retorna.

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


def main() -> None:
    n = pedir_num()
    """
    Si cualquier valor de n * n+1 (consecutivo) entre 1 y la raíz de x es
    True, devuelve True. Los números oblongos se comprueban con multiplicaciones
    consecutivas hasta la raíz del número a comprobar.
    """
    if (lambda x: any(x == n * (n + 1) for n in range(1, int(x**0.5) + 2)))(n):
        print("El número ingresado es oblongo.")
    else:
        print("El número ingresado no es oblongo.")


if __name__ == "__main__":
    main()
