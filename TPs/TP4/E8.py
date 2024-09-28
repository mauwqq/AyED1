"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""


def pedir_string() -> str:
    """Solicita al usuario que ingrese un texto y lo devuelve.

    Pre: Recibe msj, un string.

    Post: Retorna la cadena de texto ingresada por el usuario.

    """
    return input("Ingrese el texto: ")


def pedir_num() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese cuantos caracteres quiere ver de la cadena: "))
            if n > 0:
                break
            print("El número tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """Devuelve los últimos N caracteres de la cadena dada.

    Pre: cadena es la cadena de texto de la cual se extraerán los caracteres.
         n es el número de caracteres a extraer desde el final.

    Post: Retorna una subcadena que contiene los últimos n caracteres de la
          cadena.

    """
    if n > len(cadena):
        n = len(cadena)
    return "".join([cadena[i] for i in range(len(cadena) - n, len(cadena))])


def main() -> None:
    """Función principal del programa."""
    cadena = pedir_string()
    n = pedir_num()
    print(ultimos_n_caracteres(cadena, n))
    return None


if __name__ == "__main__":
    main()
