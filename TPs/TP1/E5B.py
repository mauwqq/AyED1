"""
Escribir funciones lambda para:
Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
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
    n = pedir_numero("Ingrese el numero a comprobar: ")
    if es_triangular(n):
        print("El número ingresado es triangular.")
    else:
        print("El número ingresado no es triangular.")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
