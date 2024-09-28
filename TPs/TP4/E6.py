"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el
comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es
43567890" extraer la subcadena que comienza en la posición 25 y tiene 9
caracteres, resultando la subcadena "4356-7890". Escribir una función para cada
uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def pedir_string() -> str:
    """Solicita al usuario que ingrese un texto y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna la cadena de texto ingresada por el usuario.

    """
    return input("Ingrese el texto: ")


def pedir_pos_inicial() -> int:
    """Solicita al usuario una posición inicial para extraer una subcadena.

    Pre: No recibe nada.

    Post: Retorna un número entero positivo que representa la posición inicial.
          Si el usuario ingresa un valor no válido, vuelve a solicitarlo.

    """
    while True:
        try:
            n = int(
                input(
                    "Ingrese la posición inicial desde donde se extraerá la subcadena: "
                )
            )
            if n > 0:
                break
            print("El número tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def pedir_cant_caracteres() -> int:
    """Solicita al usuario la cantidad de caracteres que se desean extraer.

    Pre: No recibe nada.

    Post: Retorna un número entero positivo que representa la cantidad de
          caracteres. Si el usuario ingresa un valor no válido, vuelve a
          solicitarlo.

    """
    while True:
        try:
            n = int(input("Ingrese la cantidad de caracteres que se extraerán: "))
            if n > 0:
                break
            print("El número tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def extraer_slicing(cadena: str, pos_inicial: int, cant_caracteres: int) -> str:
    """Extrae una subcadena de la cadena utilizando rebanadas.

    Pre: cadena es la cadena de texto de donde se extraerá,
         pos_inicial es la posición de inicio y
         cant_caracteres es la cantidad de caracteres a extraer.

    Post: Retorna la subcadena extraída como una cadena de caracteres.

    """
    return cadena[pos_inicial : pos_inicial + cant_caracteres]


def extraer_no_slicing(cadena: str, pos_inicial: int, cant_caracteres: int) -> str:
    """Extrae una subcadena de la cadena sin usar rebanadas.

    Pre: cadena es la cadena de texto de donde se extraerá,
         pos_inicial es la posición de inicio y
         cant_caracteres es la cantidad de caracteres a extraer.

    Post: Retorna la subcadena extraída como una cadena de caracteres.

    """
    resultado = ""
    for i in range(pos_inicial, pos_inicial + cant_caracteres):
        resultado += cadena[i]
    return resultado


def main() -> None:
    """Función principal del programa."""
    cadena = pedir_string()
    pos_inicial = pedir_pos_inicial()
    cant_caracteres = pedir_cant_caracteres()
    print(f"Con slicing: {extraer_slicing(cadena, pos_inicial, cant_caracteres)}")
    print(f"Sin slicing: {extraer_no_slicing(cadena, pos_inicial, cant_caracteres)}")
    return None


if __name__ == "__main__":
    main()
