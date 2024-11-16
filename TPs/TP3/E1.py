"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que
permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a
cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c.
Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f.
Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo
número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i.Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j.Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir
cualquiera sea el valor ingresado.
"""

from typing import List
from tabulate import tabulate


def pedir_num(msj: str) -> int:
    """Solicita un número entero positivo al usuario.

    Pre: msj es un string.

    Post: Retorna un número entero positivo ingresado por el usuario.

    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                return n
            raise ValueError()
        except ValueError:
            print("Debe ingresar un numero entero positivo.")


def cargar_matriz(n: int) -> List[List[int]]:
    """Carga números enteros en una matriz de n x n desde el teclado.

    Pre: n es un número entero positivo que representa el tamaño de la matriz.

    Post: Retorna una matriz de tamaño n x n llena de números enteros ingresados
          por el usuario.

    """
    matriz = []
    for i in range(n):
        fila = list(
            map(
                int,
                input(
                    f"Ingrese los elementos de la fila {i + 1} (separados por espacios): "
                ).split(),
            )
        )
        if len(fila) != n:
            print(f"Debe ingresar exactamente {n} elementos.")
            return cargar_matriz(n)
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz: List[List[int]], msj: str) -> None:
    """Imprime la matriz proporcionada en formato tabular.

    Pre: matriz es una lista de listas con valores enteros, representando una matriz.

    Post: Imprime la matriz con tabulate y no retorna valor.

    """
    print(msj)
    print(tabulate(matriz, tablefmt="grid"))
    return None


def ordenar_filas(matriz: List[List[int]]) -> None:
    """Ordena en forma ascendente cada una de las filas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.

    Post: Las filas de la matriz están ordenadas en forma ascendente.

    """
    for fila in matriz:
        fila.sort()
    return None


def intercambiar_filas(matriz: List[List[int]], f1: int, f2: int) -> bool:
    """Intercambia dos filas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.
         f1 y f2 son índices válidos de filas.

    Post: Retorna True si las filas f1 y f2 han sido intercambiadas, 
          o False si los índices son inválidos.

    """
    try:
        matriz[f1], matriz[f2] = matriz[f2], matriz[f1]
        return True
    except IndexError:
        return False


def intercambiar_columnas(matriz: List[List[int]], c1: int, c2: int) -> bool:
    """Intercambia dos columnas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.
         c1 y c2 son índices válidos de columnas.

    Post: Retorna True si las columnas c1 y c2 han sido intercambiadas,
          o False si los índices son inválidos.

    """
    try:
        for fila in matriz:
            fila[c1], fila[c2] = fila[c2], fila[c1]
            return True
    except IndexError:
        return False


def trasponer_matriz(matriz: List[List[int]]) -> None:
    """Transpone la matriz sobre sí misma.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: La matriz ha sido transpuesta (A[i][j] intercambiado con A[j][i]).

    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return None


def promedio_fila(matriz: List[List[int]], fila: int) -> float:
    """Calcula el promedio de los elementos de una fila.

    Pre: matriz es una lista de listas que representa una matriz.
         fila es un índice válido de la fila.

    Post: Retorna el promedio de los elementos de la fila especificada,
          o -1.0 si la fila es inválida.

    """
    try:
        return sum(matriz[fila]) / len(matriz[fila])
    except IndexError:
        return -1.0


def porcentaje_impares_columna(matriz: List[List[int]], columna: int) -> float:
    """Calcula el porcentaje de elementos impares en una columna.

    Pre: matriz es una lista de listas que representa una matriz.
         columna es un índice válido de la columna.

    Post: Retorna el porcentaje de elementos impares en la columna especificada,
          o -1.0 si la columna es inválida.

    """
    try:
        total_impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
        total_elementos = len(matriz)
        return (total_impares / total_elementos) * 100
    except IndexError:
        return -1.0


def es_simetrica_diagonal_principal(matriz: List[List[int]]) -> bool:
    """Determina si la matriz es simétrica respecto a su diagonal principal.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: Retorna True si la matriz es simétrica respecto a su diagonal principal,
          o False en caso contrario.

    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_diagonal_secundaria(matriz: List[List[int]]) -> bool:
    """Determina si la matriz es simétrica respecto a su diagonal secundaria.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: Retorna True si la matriz es simétrica respecto a su diagonal secundaria,
          o False en caso contrario.

    """
    n = len(matriz)
    return all(matriz[i][j] == matriz[n - j - 1][n - i - 1] for i in range(n) for j in range(n))


def columnas_palindromas(matriz: List[List[int]]) -> List[int]:
    """Determina qué columnas de la matriz son palíndromos.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: Retorna una lista con los índices de las columnas que son palíndromos.

    """
    n = len(matriz)
    palindromas = []
    for c in range(n):
        col = [matriz[r][c] for r in range(n)]
        if col == col[::-1]:
            palindromas.append(c)
    return palindromas


def main() -> None:
    """Función principal del programa."""
    n = pedir_num("Ingrese el tamaño de la matriz (n x n): ")
    matriz = cargar_matriz(n)
    imprimir_matriz(matriz, "Matriz cargada:")
    ordenar_filas(matriz)
    imprimir_matriz(matriz, "Matriz después de ordenar filas:")
    while True:
        f1, f2 = pedir_num(
            "Ingrese el primer numero de fila para intercambiar: "
            ), pedir_num(
                "Ingrese el segundo numero de fila para intercambiar: "
                )
        if not intercambiar_filas(matriz, f1-1, f2-1):
            print("Indices de filas invalido, reintentar.")
            continue
        imprimir_matriz(matriz, "Matriz después de intercambiar filas:")
        break
    while True:
        c1, c2 = pedir_num(
            "Ingrese el primer numero de columna para intercambiar: "
        ), pedir_num(
            "Ingrese el segundo numero de columna para intercambiar: "
            )
        if not intercambiar_columnas(matriz, c1-1, c2-1):
            print("Columna invalida, reintentar.")
            continue
        imprimir_matriz(matriz, "Matriz después de intercambiar columnas:")
        break
    trasponer_matriz(matriz)
    imprimir_matriz(matriz, "Matriz traspuesta:")
    while True:
        fila_promedio = pedir_num("Ingrese el número de fila para calcular su promedio: ")
        promedio = promedio_fila(matriz, fila_promedio-1)
        if promedio == -1.0:
            print("La fila ingresada es invalida.")
            continue
        print(f"El promedio de la fila {fila_promedio} es: {promedio:.2f}%" if promedio != -1.0 else None)
        break
    while True:
        columna_impares = pedir_num("Ingrese el número de columna para calcular el porcentaje de impares: ") -1
        porcentaje = porcentaje_impares_columna(matriz, columna_impares)
        if porcentaje == -1.0:
            print("La columna ingresada es invalida.")
            continue
        print(
            f"El porcentaje de elementos impares en la columna {columna_impares+1} es: {porcentaje:.2f}%" if porcentaje != -1.0 else "La columna ingresada es invalida."
        )
        break
    print(
        f"La matriz es simétrica respecto a su diagonal principal: {"Si" if es_simetrica_diagonal_principal(matriz) else "No"}"
    )
    print(
        f"La matriz es simétrica respecto a su diagonal secundaria: {"Si" if es_simetrica_diagonal_secundaria(matriz) else "No"}"
    )
    palindromas = columnas_palindromas(matriz)
    print(f"Las columnas palíndromas son: {" ".join(map(str, palindromas)) if palindromas else "No hubo columnas palindromas."}")
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
