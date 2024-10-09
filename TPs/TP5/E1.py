"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funciona-
miento de la misma.
"""


def pedir() -> int:
    """Pide un string y lo pas a validar para verificar si se cumplen las
    condiciones que se piden. Si devuelve una excepcion la imprime.

    Pre: No recibe ningún valor.

    Post: Si se produce una excepción, la imprime; si no, no imprime nada.
          Devuelve siempre un numero entero.

    """
    while True:
        try:
            return validar(input("Ingrese un número natural (Ctrl + C para salir): "))
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nSaliendo...")
            return 0


def validar(valor: str) -> int:
    """Verifica si valor no es un número o es negativo.

    Pre: Recibe valor, un string.

    Post: Devuelve valor si es un número entero positivo, sino la excepcion.

    """
    try:
        valor = int(valor)
    except ValueError as e:
        raise ValueError("Debe ingresar un número.") from e
    if valor <= 0:
        raise ValueError("El número debe ser positivo.")
    return int(valor)


def main() -> None:
    """Función principal del programa."""
    pedir()
    return None


if __name__ == "__main__":
    main()
