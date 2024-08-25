"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""


def numeros_input() -> list[int]:
    """
    Pide y guarda 3 numeros positivos.
    post -> devuelve una lista con los tres numeros.
    """
    numeros = []
    i = 1
    while len(numeros) < 3:
        try:
            numero = int(input(f"ingrese el numero {i}: "))
            if numero > 0:
                numeros.append(numero)
                i += 1
            else:
                print("El numero tiene que ser positivo.")
        except ValueError:
            print("Valor invalido, reintentar.")
    return numeros


def mayor(numeros: list[int]) -> int:
    """
    Busca el mayor estricto de los 3 y devuelve
    el numero mayor o -1 si no es el mayor estricto
    pre -> recibe una lista de enteros con los 3 numeros mayores a 0
    post -> devuelve el mayor estricto si existe, sino devuelve -1
    """
    mayor = 0
    rep = 0
    for i in numeros:
        if i > mayor:
            mayor = i
            rep = 0
        elif i == mayor:
            rep += 1
    return mayor if rep == 0 else -1


def imprimir_resultados(resultado: int) -> None:
    """
    Imprime los resultados obtenidos de los procesos anteriores
    pre -> recibe el resultado de mayor()
    post -> si el resultado es distinto a -1 imprime el mayor estricto
    """
    if resultado != -1:
        print(f"El numero mayor ingresado es: {resultado}.")
    else:
        print("No hubo ningun numero mayor estricto.")


def main() -> None:
    numeros = numeros_input()
    resultado = mayor(numeros)
    imprimir_resultados(resultado)


if __name__ == "__main__":
    main()
