"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""


def pedir_numeros() -> list[int]:
    numeros = []
    print("Ingrese los numeros.")
    for i in range(2):
        while True:
            try:
                num = int(input(f"Ingrese el numero {i+1}: "))
                if num > 0:
                    numeros.append(num)
                    break
                print("El numero no es positivo. Reintentar.")
            except ValueError:
                print("Ingrese un numero valido.")
    return numeros


def crear_lista(a: int, b: int) -> list[int]:
    """Crea una lista por comprension de numeros entre A y B que sean
    multiplos de 7 y no sean multiplos de 5.
    Formato -> Si se cumple la condicion, condicion.
    Pre -> Recibe dos numeros enteros: a y b, que determinan el rango de los
        numeros a generar.
    Post -> Devuelve una lista de los numeros de ese rango que cumplen la
        condicion necesaria.
    """
    return [e for e in range(a, b) if e % 7 == 0 and e % 5 != 0]


def imprimir_lista(lista: list[int]) -> None:
    print(" ".join(str(e) for e in lista))


def main() -> None:
    a, b = pedir_numeros()
    lista = crear_lista(a, b)
    print(
        f"Los numeros entre {a} y {b} multiplos de 7 y no multiplos de 5 son: ",
    )
    imprimir_lista(lista)


if __name__ == "__main__":
    main()
