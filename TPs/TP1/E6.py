"""
Desarrollar una función que reciba como parámetros dos números enteros
positivos y devuelva como valor de retorno el número que resulte de
concatenar ambos parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver
1234567. No se permite utilizar facilidades de Python no vistas en clase.
"""


def pedir_numero(msj: str) -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                break
            print("El número ingresado tiene que ser positivo.")
        except ValueError:
            print("Carácter inválido, reintentar.")
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
