"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades
producidas en cada una de sus plantas durante una semana. De este modo, cada
columna representa el día de la semana y cada fila a una de sus fábricas.
Se solicita:
    a. Crear una matriz con datos generados al azar para N fábricas durante una
        semana, considerando que la capacidad máxima de fabricación es de 150
        unidades por día y puede suceder que en ciertos días no se fabrique nin
        guna.
    b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
    c. Cuál es la fábrica que más produjo en un solo día (detallar día y
        fábrica).
    d. Cuál es el día más productivo, considerando todas las fábricas
        combinadas.
    e. Crear una lista por comprensión que contenga la menor cantidad fabricada
        por cada fábrica.
"""

import random as rn
from typing import List, Tuple

dias = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5: "Sabado"}


def pedir_cantidad_fabricas() -> int:
    """Solicita al usuario la cantidad de fábricas.

    Pre: No recibe nada.

    Post: Devuelve un número entero "n" que representa la cantidad
          de fábricas, asegurándose de que sea positivo.

    """
    while True:
        try:
            n = int(input("Ingrese la cantidad de fabricas: "))
            if n > 0:
                return n
            print("El numero debe ser positivo.")
        except ValueError:
            print("Debe ingresar un numero.")


def gen_produccion() -> int:
    """Genera una cantidad aleatoria de producción.

    Pre: No recibe nada.

    Post: Devuelve un número entero aleatorio entre 0 y 150,
          representando la producción diaria.

    """
    return rn.randint(0, 150)


def gen_matriz(n: int) -> List[List[int]]:
    """Genera una matriz de producción para las fábricas.

    Pre: Recibe un entero "n" que representa la cantidad de fábricas.

    Post: Devuelve una matriz con la producción diaria generada
          aleatoriamente.

    """
    return [[gen_produccion() for _ in range(len(dias))] for _ in range(n)]


def total_fabricacion(matriz: List[List[int]]) -> List[int]:
    """Calcula el total de bicicletas fabricadas por cada fábrica.

    Pre: Recibe una matriz de producción.

    Post: Devuelve una lista con la suma total de producción
          por cada fábrica.

    """
    return [sum(x) for x in matriz]


def imprimir_resultados(matriz: List[List[int]], total: List[int]) -> None:
    """Imprime la producción de cada fábrica y sus totales.

    Pre: Recibe una matriz de producción y una lista de totales.

    Post: Imprime en consola los resultados de producción
          por fábrica junto a sus totales.

    """
    print(
        "\n".join(
            f"fabrica {i+1}: {" ".join(map(str, produccion)):<25}\tTOTAL: {total[i]}"
            for i, produccion in enumerate(matriz)
        )
    )
    return None


def mayor_produccion_un_dia(matriz: List[List[int]]) -> Tuple[int, int]:
    """Encuentra la fábrica y el día con mayor producción.

    Pre: Recibe una matriz de producción.

    Post: Devuelve una tupla con el índice de la fábrica y
          el índice del día donde se produjo la mayor cantidad.

    """
    produccion_max = max(max(x) for x in matriz)
    i_fabrica = next(i for i, f in enumerate(matriz) if max(f) == produccion_max)
    i_dia = matriz[i_fabrica].index(produccion_max)
    return i_fabrica, i_dia


def dia_mas_productivo(matriz: List[List[int]]) -> int:
    """Determina el día más productivo entre todas las fábricas.

    Pre: Recibe una matriz de producción.

    Post: Devuelve el índice del día más productivo considerando
          la producción total de todas las fábricas.

    """
    produccion_dias = [sum([fabrica[dia] for fabrica in matriz]) for dia in dias]
    i_dia_max = produccion_dias.index(max(produccion_dias))
    return i_dia_max


def menor_cant_fabrica(matriz: List[List[int]]) -> List[int]:
    """Encuentra la menor cantidad fabricada por cada fábrica.

    Pre: Recibe una matriz de producción.

    Post: Devuelve una lista con la menor cantidad producida
          por cada fábrica en la semana.

    """
    return [min(fabrica) for fabrica in matriz]


def main() -> None:
    """Función principal del programa."""
    n = pedir_cantidad_fabricas()
    matriz = gen_matriz(n)
    total = total_fabricacion(matriz)
    imprimir_resultados(matriz, total)
    i_fabrica, i_dia = mayor_produccion_un_dia(matriz)
    print(f"La fábrica {i_fabrica+1} fue la que más produjo, el día {dias.get(i_dia)}.")
    i_dia_max = dia_mas_productivo(matriz)
    print(f"El día más productivo fue el {dias.get(i_dia_max)}.")
    return None


if __name__ == "__main__":
    main()
