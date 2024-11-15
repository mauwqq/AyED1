"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""

import random as rn


def pedir_num() -> int:
    """Pide un numero al usuario y lo devuelve.

    Pre: No recibe nada.

    Post: Devuelve n un numero entero.

    """
    while True:
        try:
            n = input("Ingrese un numero entero entre 1 y 500 para adivinar: ").strip()
            if not n.isdigit():
                raise ValueError("Debe ingresar un numero.")
            break
        except ValueError as e:
            print(e)
    return n


def gen_numero() -> int:
    """Genera un numero aleatorio entre 1 y 500 y lo devuelve.

    Pre: No recibe nada.

    Post: Devuelve un entero entre 1 y 500 generado aleatoriamente.

    """
    return rn.randint(1, 500)


def adivinar_numero(random: int) -> int:
    """Cuenta cuantos intentos le llevo al jugador adivinar el numero generado
    ademas cada vez que el jugador ingresa un numero, le informa si ese numero
    es mayor o menor al numero que esta intentando adivinar.

    Pre: random es el numero entero positivo generado entre 1 y 500.

    Post: Devuelve la cantidad de intentos que le tomo al usuario adivinar el
          numero.

    """
    intentos = 0
    while True:
        n = pedir_num()
        intentos += 1
        if n == random:
            break
        if n > random:
            print(f"{n} es mayor que el numero a adivinar.")
        else:
            print(f"{n} es menor que el numero a adivinar.")
    return intentos


def imprimir_resultados(random: int, intentos: int) -> None:
    """Imprime el numero generado y la cantidad de intentos que le tomo
    al usuario adivinarlo.

    Pre: random es un entero positivo.
         intentos es un entero positivo.

    Post: No devuelve nada.

    """
    print(f"El numero es {random} y llevo {intentos} intentos.")
    return None


def main() -> None:
    """Función principal del programa."""
    random = gen_numero()
    # print(random)
    intentos = adivinar_numero(random)
    imprimir_resultados(random, intentos)


if __name__ == "__main__":
    main()
