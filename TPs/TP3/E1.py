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


def cargar_matriz(n: int) -> list[list[int]]:
    """Carga números enteros en una matriz de N x N desde el teclado.

    Pre: n es un número entero positivo que representa el tamaño de la matriz.

    Post: Retorna una matriz de tamaño N x N llena de números enteros ingresados
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
            print("Error: Debe ingresar exactamente N elementos.")
            return cargar_matriz(n)
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """Imprime la matriz en formato legible.

    Pre: matriz es una lista de listas que representa una matriz.

    Post: Imprime la matriz en la consola.

    """
    for fila in matriz:
        print(" ".join(map(str, fila)))
    print()


def ordenar_filas(matriz: list[list[int]]) -> None:
    """Ordena en forma ascendente cada una de las filas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.

    Post: Las filas de la matriz están ordenadas en forma ascendente.
    
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: list[list[int]], f1: int, f2: int) -> None:
    """Intercambia dos filas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.
         f1 y f2 son índices válidos de filas.

    Post: Las filas f1 y f2 han sido intercambiadas en la matriz.

    """
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]


def intercambiar_columnas(matriz: list[list[int]], c1: int, c2: int) -> None:
    """Intercambia dos columnas de la matriz.

    Pre: matriz es una lista de listas que representa una matriz.
         c1 y c2 son índices válidos de columnas.

    Post: Las columnas c1 y c2 han sido intercambiadas en la matriz.

    """
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]


def trasponer_matriz(matriz: list[list[int]]) -> None:
    """Transpone la matriz sobre sí misma.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: La matriz ha sido transpuesta (A[i][j] intercambiado con A[j][i]).

    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """Calcula el promedio de los elementos de una fila.

    Pre: matriz es una lista de listas que representa una matriz.
         fila es un índice válido de la fila.

    Post: Retorna el promedio de los elementos de la fila especificada.

    """
    return sum(matriz[fila]) / len(matriz[fila])


def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:
    """Calcula el porcentaje de elementos impares en una columna.

    Pre: matriz es una lista de listas que representa una matriz.
         columna es un índice válido de la columna.

    Post: Retorna el porcentaje de elementos impares en la columna especificada.

    """
    total_impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
    total_elementos = len(matriz)
    return (total_impares / total_elementos) * 100


def es_simetrica_diagonal_principal(matriz: list[list[int]]) -> bool:
    """Determina si la matriz es simétrica respecto a su diagonal principal.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: Retorna True si la matriz es simétrica respecto a su diagonal principal,
          de lo contrario retorna False.

    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_diagonal_secundaria(matriz: list[list[int]]) -> bool:
    """Determina si la matriz es simétrica respecto a su diagonal secundaria.

    Pre: matriz es una lista de listas que representa una matriz cuadrada.

    Post: Retorna True si la matriz es simétrica respecto a su diagonal secundaria,
          de lo contrario retorna False.

    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return False
    return True


def columnas_palindromas(matriz: list[list[int]]) -> list[int]:
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
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz = cargar_matriz(n)
    print("Matriz cargada:")
    imprimir_matriz(matriz)
    ordenar_filas(matriz)
    print("Matriz después de ordenar filas:")
    imprimir_matriz(matriz)
    f1, f2 = map(
        int,
        input("Ingrese dos números de fila para intercambiar (0-indexed): ").split(),
    )
    intercambiar_filas(matriz, f1, f2)
    print("Matriz después de intercambiar filas:")
    imprimir_matriz(matriz)
    c1, c2 = map(
        int,
        input("Ingrese dos números de columna para intercambiar (0-indexed): ").split(),
    )
    intercambiar_columnas(matriz, c1, c2)
    print("Matriz después de intercambiar columnas:")
    imprimir_matriz(matriz)
    trasponer_matriz(matriz)
    print("Matriz traspuesta:")
    imprimir_matriz(matriz)
    fila_promedio = int(
        input("Ingrese el número de fila para calcular su promedio (0-indexed): ")
    )
    promedio = promedio_fila(matriz, fila_promedio)
    print(f"El promedio de la fila {fila_promedio} es: {promedio}")
    columna_impares = int(
        input(
            "Ingrese el número de columna para calcular el porcentaje de impares (0-indexed): "
        )
    )
    porcentaje = porcentaje_impares_columna(matriz, columna_impares)
    print(
        f"El porcentaje de elementos impares en la columna {columna_impares} es: {porcentaje:.2f}%"
    )
    simetrica_principal = es_simetrica_diagonal_principal(matriz)
    print(
        f"La matriz es simétrica respecto a su diagonal principal: {simetrica_principal}"
    )
    simetrica_secundaria = es_simetrica_diagonal_secundaria(matriz)
    print(
        f"La matriz es simétrica respecto a su diagonal secundaria: {simetrica_secundaria}"
    )
    columnas_pal = columnas_palindromas(matriz)
    print(f"Las columnas palíndromas son: {columnas_pal}")


if __name__ == "__main__":
    main()
