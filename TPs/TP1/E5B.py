"""
Escribir funciones lambda para:
Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
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


def es_triangular(n: int) -> bool:
    """Determina si un número es un número triangular.
    Un número triangular es aquel que puede representarse
    como la suma de los primeros n números naturales.
    La fórmula para el n-ésimo número triangular es:
    T = n * (n + 1) / 2.

    Pre: n es un entero no negativo.

    Post: Retorna True si n es un número triangular,
          y False en caso contrario.

    """
    return (
        lambda x: any(n * (n + 1) // 2 == x for n in range(1, int((2 * x) ** 0.5) + 1))
    )(n)


def main() -> None:
    """Función principal del programa."""
    n = pedir_num()
    if es_triangular(n):
        print("El número ingresado es triangular.")
    else:
        print("El número ingresado no es triangular.")
    return None


if __name__ == "__main__":
    main()
