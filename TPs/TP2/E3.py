"""
Crear una lista con los cuadrados de los números entre 1 y N
(ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita
imprimir los últimos 10 valores de la lista.
"""


def pedir_numero() -> int:
    while True:
        try:
            n = int(input(
                "Ingrese un numero entero positivo: ",
                ))
            if n > 0:
                break
            print("El numero debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un numero entero.")
    return n


def crear_lista(longitud: int) -> list[int]:
    """Crea la lista con la longitud dada en un numero entero.
    Pre -> Recibe la longitud de la lista a crear.
    Post -> Crea una lista por comprension con la longitud dada.
    """
    return [x for x in range(1,longitud+1)]


def cuadrado_lista(lista: list[int]) -> list[int]:
    """Calcula el cuadrado de todos los numeros en la lista.
    Pre -> Recibe la lista de enteros positivos.
    Post -> Crea una lista con map y una funcion lambda que multiplica
        cada valor de la lista por el mismo y lo guarda.
    """
    return list(map(lambda x: x * x, lista))


def imprimir_lista(lista: list[int]) -> None:
    """Imprime los ultimos 10 numeros cuadrados de la lista.
    Pre -> Recibe la lista de numeros enteros.
    Post -> Devuelve los ultimos 10 numeros de la lista formateados.
    """
    print("Ultimos 10 numeros cuadrados:")
    print("\n".join([f"{i+1}: {num}" for i, num in enumerate(lista[-10:])]))
    return None


def main() -> None:
    longitud = pedir_numero()
    lista_gen = crear_lista(longitud)
    lista_cuadrado = cuadrado_lista(lista_gen)
    imprimir_lista(lista_cuadrado)


if __name__ == '__main__':
    main()
