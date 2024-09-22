"""
Desarrollar una función que determine si una cadena de caracteres es capicúa,
sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que
permita verificar su funcionamiento.
"""

def es_capicua(cadena: str):
    """Determina si la cadena dada es capicúa.

    Pre: La cadena es de tipo str.

    Post: Retorna True si la cadena es capicúa; de lo contrario, retorna False.
    """
    inicio = 0
    fin = len(cadena) - 1
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


def main() -> None:
    while True:
        cadena = input("Introduce una cadena de caracteres (0 para salir): ")
        if cadena == '0':
            break
        if es_capicua(cadena):
            print(f"La cadena '{cadena}' es capicúa.")
        else:
            print(f"La cadena '{cadena}' no es capicúa.")


if __name__ == "__main__":
    main()
