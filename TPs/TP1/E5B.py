"""
Escribir funciones lambda para:
Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
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
    """Función principal que verifica si un número es triangular.

    Post: Solicita un número entero positivo al usuario y comprueba si es un
          número triangular. Un número es triangular si existe un entero n
          tal que n * (n + 1) / 2 es igual al número ingresado.

    """
    n = pedir_num()
    if (lambda x: any(n * (n + 1) // 2 == x for n in range(1, int((2 * x)**0.5) + 1)))(n):
        print("El número ingresado es triangular.")
    else:
        print("El número ingresado no es triangular.")


if __name__ == "__main__":
    main()
