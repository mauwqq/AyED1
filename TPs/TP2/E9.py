"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""


def pedir_numeros() -> list[int]:
    """Solicita al usuario ingresar dos números enteros positivos.

    Post: Devuelve una lista de dos números enteros positivos ingresados por el
          usuario.
          Si se ingresa un valor no positivo o no entero, solicita el ingreso
          nuevamente.

    """
    numeros = []
    print("Ingrese los números.")
    for i in range(2):
        while True:
            try:
                num = int(input(f"Ingrese el número {i+1}: "))
                if num > 0:
                    numeros.append(num)
                    break
                print("El número no es positivo. Reintentar.")
            except ValueError:
                print("Ingrese un número válido.")
    return numeros


def crear_lista(a: int, b: int) -> list[int]:
    """Crea una lista de números entre A y B que son múltiplos de 7 y no múltiplos de 5.

    Pre: Recibe dos números enteros "a" y "b", que determinan el rango de
         números a generar.

    Post: Devuelve una lista de enteros que contiene los números en el
          rango [a, b) que son múltiplos de 7 y no son múltiplos de 5.

    """
    return [e for e in range(a, b) if e % 7 == 0 and e % 5 != 0]


def imprimir_lista(lista: list[int]) -> None:
    """Imprime los elementos de la lista.

    Pre: Recibe una lista de enteros.

    Post: Imprime los elementos de la lista, separados por espacios.

    """
    print(" ".join(str(e) for e in lista))


def main() -> None:
    a, b = pedir_numeros()
    lista = crear_lista(a, b)
    print(
        f"Los números entre {a} y {b} múltiplos de 7 y no múltiplos de 5 son: ",
    )
    imprimir_lista(lista)


if __name__ == "__main__":
    main()
