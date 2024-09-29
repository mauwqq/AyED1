"""
Desarrollar una función que reciba como parámetros dos números enteros
positivos y devuelva como valor de retorno el número que resulte de
concatenar ambos parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver
1234567. No se permite utilizar facilidades de Python no vistas en clase.
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


def concatenar_numeros(n1: int, n2: int) -> int:
    """Concatena dos números enteros positivos y lo devuelve.

    Pre: Recibe dos números enteros positivos.

    Post: Concatena los números casteandolos a string, uniéndolos
          y devolviendo la unión de estos en un entero.

    """
    return int(str(n1) + str(n2))


def main() -> None:
    """Función principal del programa."""
    n1 = pedir_numero("Ingrese el primer numero: ")
    n2 = pedir_numero("Ingrese el segundo numero: ")
    resultado = concatenar_numeros(n1, n2)
    print(f"El numero concatenado es: {resultado}")
    return None


if __name__ == "__main__":
    main()
