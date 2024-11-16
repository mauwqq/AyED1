"""
Desarrollar una función que reciba tres números enteros positivos
correspondientes al día, mes, año de una fecha y verifique si corresponden a
una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes,
incluyendo los años bisiestos. Devolver True o False según la fecha sea
correcta o no. Realizar también un programa para verificar el comportamiento
de la función.
"""

from typing import List


meses = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def recibir_numeros() -> List[int]:
    """Pide tres números enteros positivos, los guarda en una lista y
    devuelve la lista.

    Pre: No recibe nada.

    Post: Devuelve una lista de tres enteros que corresponden
          al día, mes y año solicitado.

    """
    fecha = []  # dia, mes, año
    texto = ["Dia", "Mes", "Año"]
    print("Ingrese la fecha en el formato indicado.")
    while len(fecha) < 3:
        try:
            num = input(f"{texto[len(fecha)]}: ").strip()
            if not num.isdigit():
                raise ValueError("Debe ser un numero.")
            if int(num) > 0:
                fecha.append(num)
                continue
            raise ValueError("Debe ser un numero positivo.")
        except ValueError as e:
            print(e)
    return [int(i) for i in fecha]


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.

    Pre: Recibe el año como un número entero.

    Post: Si el entero es divisible por cuatro y no es divisible
          por 100, o es divisible por 400 es bisiesto y devuelve True, si no False.

    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Válida si una fecha especificada por día, mes y año es correcta.

    Pre: Recibe tres parámetros enteros positivos, que corresponden al día, mes
         y año.

    Post: Devuelve True si la fecha es válida.
          Devuelve False si la fecha no es válida.

    """
    if es_bisiesto(anio):
        meses.update({2: 29})
    return (mes in meses) and (dia <= meses.get(mes))


def imprimir_resultado(dia: int, mes: int, anio: int) -> None:
    """Imprime el resultado de validar la fecha.

    Pre: dia, mes y anio son variables enteras.

    Post: No devuelve nada.

    """
    if validar_fecha(dia, mes, anio):
        print("La fecha es valida.")
    else:
        print("La fecha no es valida.")
    return None


def main() -> None:
    """Función principal del programa."""
    dia, mes, anio = recibir_numeros()  # Desempaquetado.
    imprimir_resultado(dia, mes, anio)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
