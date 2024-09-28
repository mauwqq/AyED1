"""
Los números de claves de dos cajas fuertes están intercalados dentro de un
número entero llamado "clave maestra", cuya longitud no se conoce. Realizar un
programa para obtener ambas claves, donde la primera se construye con los
dígitos ubicados en posiciones impares de la clave maestra y la segunda con los
dígitos ubicados en posiciones pares. Los dígitos se numeran desde la izquierda.
Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería
89.
"""

import random as rn
from typing import List


def generar_numero() -> int:
    """Genera un número aleatorio entre 100 y 999999.

    Pre: No recibe parámetros.

    Post: Retorna un entero que representa un número aleatorio en el rango
          especificado.

    """
    return rn.randint(100, 999999)


def impares(n: int) -> List[int]:
    """Devuelve una lista de los dígitos en posiciones impares de un número.

    Pre: n es un entero del cual se extraen los dígitos.

    Post: Retorna una lista de enteros que representan los dígitos en posiciones
          impares del número dado.

    """
    return [valor for i, valor in enumerate(str(n)) if i % 2 != 0]


def pares(n: int) -> List[int]:
    """Devuelve una lista de los dígitos en posiciones pares de un número.

    Pre: n es un entero del cual se extraen los dígitos.

    Post: Retorna una lista de enteros que representan los dígitos en posiciones
          pares del número dado.

    """
    return [valor for i, valor in enumerate(str(n)) if i % 2 == 0]


def main() -> None:
    """Función principal del programa."""
    n = generar_numero()
    print(f"El numero generado es: {n}")
    passwd_impares = impares(n)
    passwd_pares = pares(n)
    print("la contraseña par es:", "".join(passwd_pares))
    print("la contraseña impar es:", "".join(passwd_impares))
    return None


if __name__ == "__main__":
    main()
