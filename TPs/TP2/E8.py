"""
Utilizar la técnica de listas por comprensión para construir una lista con todos
los números impares comprendidos entre 100 y 200.
"""


def crear_lista() -> list[int]:
    return [e for e in range(100,201) if e % 2 != 0]


def imprimir_lista(lista: list[int]) -> None:
    print(" ".join(str(e) for e in lista))


def main():
    lista = crear_lista()
    imprimir_lista(lista)


if __name__ == '__main__':
    main()
