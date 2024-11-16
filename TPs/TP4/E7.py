"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena
resultante. Escribir también un programa para verificar el comportamiento de la
misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def pedir_string() -> str:
    """Solicita al usuario que ingrese un texto y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna la cadena de texto ingresada por el usuario.

    """
    return input("Ingrese el texto: ")


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
            raise ValueError("Debe ingresar un número entero positivo.")
        except ValueError:
            print("Debe ingresar un número entero positivo.")
    return n


def eliminar_slicing(cadena: str, pos_inicial: int, cant_caracteres: int) -> str:
    """Elimina una subcadena de la cadena usando rebanadas.

    Pre: cadena es la cadena de texto de la cual se eliminará una subcadena.
         pos_inicial es la posición desde donde se comenzará a eliminar.
         cant_caracteres es la cantidad de caracteres que se eliminarán.

    Post: Retorna una nueva cadena que consiste en la parte de la cadena original
          antes de pos_inicial y la parte después de la subcadena eliminada.

    """
    return cadena[:pos_inicial] + cadena[pos_inicial + cant_caracteres :]


def eliminar_sin_slicing(cadena: str, pos_inicial: int, cant_caracteres: int) -> str:
    """Elimina una subcadena de la cadena sin usar rebanadas.

    Pre: cadena es la cadena de texto de la cual se eliminará una subcadena.
         pos_inicial es la posición desde donde se comenzará a eliminar.
         cant_caracteres es la cantidad de caracteres que se eliminarán.

    Post: Retorna una nueva cadena construida sin la subcadena especificada.
          Esta cadena se genera mediante la concatenación de los caracteres
          que no se encuentran en el rango de eliminación.

    """
    resultado = ""
    for i in range(len(cadena)):
        if i < pos_inicial or i >= pos_inicial + cant_caracteres:
            resultado += cadena[i]
    return resultado


def main() -> None:
    """Función principal del programa."""
    cadena = pedir_string()
    pos_inicial = pedir_numero(
        "Ingrese la posicion inicial desde donde se extraera la subcadena: "
    )
    cant_caracteres = pedir_numero(
        "Ingrese la cantidad de caracteres que se extraeran: "
    )
    print(f"Con slicing: {eliminar_slicing(cadena, pos_inicial, cant_caracteres)}")
    print(f"Sin slicing: {eliminar_sin_slicing(cadena, pos_inicial, cant_caracteres)}")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
