"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?

R: Para hacer que el programa funcione para numeros mayores a 3999 habria que
usar mas simbolos romanos que aplican para cantidades mas grandes de numeros.
"""

romanos = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese un numero entre 0 y 3999 para convertir: "))
            if n > 0 and n < 4000:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero positivo entre 0 y 3999.")
    return n


def int_a_romano(numero: int) -> str:
    """Convierte un número entero entre 0 y 3999 en su equivalente a número
    romano.

    Pre: El numero debe estar en el rango de 0 a 3999

    Post: Devuelve una string equivalente al número romano.

    """
    return "".join(
        romano
        for valor, romano in romanos
        for _ in range(numero // valor)
        if (numero := numero - valor) >= 0
    )


def main() -> None:
    """Función principal del programa."""
    convertir = pedir_numero()
    num_romano = int_a_romano(convertir)
    print(num_romano)
    return None


if __name__ == "__main__":
    main()
