"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""


def centrar_cadena(cadena: str) -> str:
    """Imprime la cadena centrada en 80 columnas.

    Pre: La cadena es un objeto de tipo str.

    Post: La cadena se devuelve centrada.

    """
    return cadena.center(80)


def main() -> None:
    """Función principal del programa."""
    cadena = input("Introduce una cadena de caracteres: ")
    print(centrar_cadena(cadena))
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
