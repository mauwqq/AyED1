"""
Desarrollar una función que reciba como parámetros dos números enteros
positivos y devuelva como valor de retorno el número que resulte de
concatenar ambos parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver
1234567. No se permite utilizar facilidades de Python no vistas en clase.
"""


def pedir_numero(msj: str) -> int:
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                break
            print("El numero ingresado tiene que ser positivo.")
        except ValueError:
            print("Caracter invalido, reintentar.")
    return n


def concatenar_numeros(n1: int, n2: int) -> int:
    """Concatena dos numeros enteros positivos y lo devuelve.
    Pre -> Recibe dos numeros enteros positivos
    Post -> Concatena los numeros casteandolos a string, uniendolos
        y devolviendo la union de estos en un entero.
    """
    resultado = str(n1) + str(n2)
    return int(resultado)


def main() -> None:
    n1 = pedir_numero("Ingrese el primer numero: ")
    n2 = pedir_numero("Ingrese el segundo numero: ")
    resultado = concatenar_numeros(n1, n2)
    print(f"El numero concatenado es: {resultado}")


if __name__ == "__main__":
    main()
