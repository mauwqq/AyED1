"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""


def centrar_cadena(cadena: str) -> None:
    """Imprime la cadena centrada en 80 columnas.

    Pre: La cadena es un objeto de tipo str.

    Post: La cadena se imprime en el centro de una línea de 80 columnas.
    """
    ancho = 80
    cadena_centrada = cadena.center(ancho)
    print(cadena_centrada)


def main() -> None:
    cadena = input("Introduce una cadena de caracteres: ")
    centrar_cadena(cadena)


if __name__ == "__main__":
    main()
