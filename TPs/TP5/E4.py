"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""


def imprimir_numeros(ult: int = 1) -> None:
    """Imprime los números enteros desde 'ult' hasta 100,000. Si se interrumpe
    el programa mediante Ctrl-C, se solicita al usuario confirmar si desea
    continuar imprimiendo o salir.

    Pre: ult es un numero entero: El número entero desde el cual comenzar a imprimir.
         Por defecto es 1.

    Post: Devuelve None.

    """
    try:
        for i in range(ult, 100001):
            print(i)
    except KeyboardInterrupt:
        while True:
            match input(
                "Se detecto una interrupcion por teclado\nConfirmar(S/N): "
            ).upper():
                case "S":
                    print("Saliendo...")
                    break
                case "N":
                    imprimir_numeros(i)
                    break
                case _:
                    print("Opción no válida. Por favor, ingrese 'S' o 'N'.")
    return None


def main() -> None:
    """Función principal del programa."""
    imprimir_numeros()
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
