"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
"""

from functools import reduce


def pedir_num() -> int:
    while True:
        try:
            n = int(input("Ingrese el numero a comprobar: "))
            if n > 0:
                return n
            print("El numero debe ser positivo.")
        except ValueError:
            print("Debe ingresar un numero.")


def main() -> None:
    n = pedir_num()
    """
    Si cualquier valor de n * n+1 (consecutivo) entre 1 y la raiz de x es
    True, devuelve True. Los numeros oblongos se comprueban con multiplicaciones
    consecutivas hasta la raiz del numero a comprobar.
    """
    es_oblongo = lambda x: any(x == n * (n + 1) for n in range(1, int(x**0.5) + 2))
    if es_oblongo(n):
        print("El numero ingresado es oblongo.")
    else:
        print("El numero ingresado no es oblongo.")


if __name__ == "__main__":
    main()
