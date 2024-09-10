"""
Intercalar los elementos de una lista entre los elementos de otra. La
intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas
y no se creará una lista nueva sino que se modificará la primera. Por ejemplo,
si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como
[8, 5, 1, 9, 3, 7]. Las listas pueden tener distintas longitudes.
"""

import random as rn


def crear_lista() -> list[int]:
    return [rn.randint(1, 10) for _ in range(rn.randint(5, 10))]


def mezclar_listas(lista1: list[int], lista2: list[int]) -> None:
    """Mezcla las listas usando slicing, itera la longitud de la menor lista,
    usando min(). cuando start:stop son iguales en el slicing, es como una
    posicion de insercion. En realidad estoy insertado una lista adentro de
    lista1, por eso tengo que pasar el valor de lista2 como: [lista2[i]],
    tiene que ser un iterable, a su vez:
        i = 0 -> 2 * 0 + 1 = 1
        i = 1 -> 2 * 1 + 1 = 2
        i = 2 -> 2 * 2 + 1 = 5
    Extend añade los numeros restante si la lista2 es mas larga que la 1.
    Pre -> Recibe dos listas de enteros.
    Post -> Devuelve una lista de las dos brindadas.
    """
    long = min(len(lista1), len(lista2))
    extend = len(lista2) > len(lista1)
    for i in range(long):
        lista1[2 * i + 1 : 2 * i + 1] = [lista2[i]]
    if extend:
        lista1.extend(lista2[long:])


def imprimir_lista(lista: list[int], msj) -> None:
    print(msj)
    print(" ".join(str(e) for e in lista))


def main():
    lista1 = crear_lista()
    imprimir_lista(lista1, "Primera lista:")
    lista2 = crear_lista()
    imprimir_lista(lista2, "Segunda lista:")
    mezclar_listas(lista1, lista2)
    imprimir_lista(lista1, "Lista intercalada:")


if __name__ == "__main__":
    main()