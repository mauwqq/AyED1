"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres
conteniendo una frase y un entero N, y devuelva otra cadena con las palabras
que tengan N o más caracteres de la cadena original. Escribir también un
programa para verificar el comportamiento de la misma. Hacer tres versiones de
la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""


def pedir_string() -> str:
    """Solicita al usuario que ingrese una oración.

    Pre: No recibe nada.

    Post: Retorna la cadena de texto ingresada por el usuario.

    """
    return input("Ingrese una oracion: ")


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: No recibe nada.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese un numero positivo: "))
            if n > 0:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero positivo.")
    return n


def filtrar_palabras_comprension(cadena: str, n: int) -> str:
    """Filtra las palabras de una cadena que tienen más de n caracteres
    utilizando comprensión de listas.

    Pre: cadena es una cadena de texto y n es un entero.

    Post: Retorna una cadena con las palabras filtradas separadas por espacios.

    """
    return " ".join([palabra for palabra in cadena.split(" ") if len(palabra) > n])


def filtrar_palabras_filter(cadena: str, n: int) -> str:
    """Filtra las palabras de una cadena que tienen más de n caracteres
    utilizando la función filter.

    Pre: cadena es una cadena de texto y n es un entero.

    Post: Retorna una cadena con las palabras filtradas separadas por espacios.

    """
    return " ".join(filter(lambda x: x if len(x) > n else None, cadena.split(" ")))


def filtrar_palabras_ciclos(cadena: str, n: int) -> str:
    """Filtra las palabras de una cadena que tienen más de n caracteres
    utilizando un bucle for.

    Pre: cadena es una cadena de texto y n es un entero.

    Post: Retorna una cadena con las palabras filtradas separadas por espacios.

    """
    resultado = []
    for palabra in cadena.split(" "):
        if len(palabra) > n:
            resultado.append(palabra)
    return " ".join(resultado)


def main() -> None:
    """Función principal del programa."""
    cadena = pedir_string()
    num = pedir_numero()
    print(f"Por comprensión: {filtrar_palabras_comprension(cadena, num)}")
    print(f"Con filter(): {filtrar_palabras_filter(cadena, num)}")
    print(f"Por ciclos normales: {filtrar_palabras_ciclos(cadena, num)}")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
