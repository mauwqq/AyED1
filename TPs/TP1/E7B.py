"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres
enteros correspondientes el día siguiente al dado. Utilizando esta función
sin modificaciones ni agregados, desarrollar programas que permitan:
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
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


def pedir_fecha(msj: str) -> List[int]:
    """Solicita la fecha al usuario verificado cada valor ingresado. Primero
    solicita el año, si es bisiesto actualiza la cantidad de dias de febrero en
    meses. Despues solicita el mes que comprueba con comprobar_mes y por ultimo
    solicita el dia.

    Pre: Recibe un string.

    Post: Devuelve una lista de tres enteros con la fecha en formato YY/MM/DD.

    """
    fecha = []
    texto = ["Año", "Mes", "Dia"]
    print(msj)
    for i in range(3):
        while True:
            try:
                num = int(input(f"{texto[i]}: "))
                if num > 0:
                    match i:
                        case 0:  # año
                            fecha.append(num)
                            if es_bisiesto(num):
                                meses.update({2: 29})
                        case 1:  # mes
                            if comprobar_mes(num):
                                fecha.append(num)
                            else:
                                print("Mes invalido, reintentar.")
                                continue
                        case 2:  # dia
                            if comprobar_dia(num, fecha[1]):
                                fecha.append(num)
                            else:
                                print("Dia invalido, reintentar.")
                                continue
                    break
                raise ValueError()
            except ValueError:
                print("Debe ingresar un numero positivo, reintentar.")
    return fecha


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.

    Pre: Recibe el año como un número entero.

    Post: Si el entero es divisible por cuatro y no es divisible
          por 100, o es divisible por 400 es bisiesto y devuelve True, si no False.

    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def comprobar_mes(mes: int) -> bool:
    """Comprueba si el mes dado como parámetro es válido.

    Pre: Recibe el mes como un número entero positivo.

    Post: Si el número está en las claves del diccionario, meses devuelve True.
          Si el número no está en las claves del diccionario, meses devuelve
          False.

    """
    return mes in meses


def comprobar_dia(dia: int, mes: int) -> bool:
    """Comprueba que el día ingresado por el usuario sea válido verificando que
    sea menor o igual al valor del mes en meses.

    Pre: día es un número entero positivo.
         mes es un número entero positivo.

    Post: Devuelve True si día es menor o igual a la cantidad de días del mes.
          Devuelve False si día es mayor a la cantidad de días del mes.

    """
    return dia <= meses.get(mes)


def diasiguiente(anio: int, mes: int, dia: int) -> List[int]:
    """Suma un día a la fecha ingresada.

    Pre: dia, mes y anio son números enteros positivos.

    Post: Devuelve una tupla de tres enteros(dia, mes, año) con la fecha
          modificada.

    """
    if (dia + 1) < meses.get(mes):
        dia += 1
    else:
        if mes != 12:
            mes += 1
            dia = 1
        else:
            anio += 1
            mes = 1
            dia = 1
    return [anio, mes, dia]


def diferencia_dias(fecha: list[int], fecha2: list[int]) -> int:
    """Cuenta cuantos días falta para llegar a la segunda fecha, primero
    comprueba cuál fecha es la más antigua para hacer la cuenta de atrás a
    adelante, y suma el contador.

    Pre: fecha es una lista de tres números enteros positivos.
         fecha2 es una lista de tres números enteros positivos.

    Post: Devuelve la cantidad de días que faltan para llegar a la segunda fecha
          un número entero positivo.

    """
    dif = 0
    si_fecha2_antigua = (fecha2[0] < fecha[0]) or (fecha2[1] < fecha[1])
    while fecha != fecha2:
        if si_fecha2_antigua:
            fecha2 = diasiguiente(fecha2[0], fecha2[1], fecha2[2])
        else:
            fecha = diasiguiente(fecha[0], fecha[1], fecha[2])
        dif += 1
    return dif


def main() -> None:
    """Función principal del programa."""
    fecha = pedir_fecha("Ingrese la primera fecha: ")
    fecha2 = pedir_fecha("Ingrese la segunda fecha: ")
    dif = diferencia_dias(fecha, fecha2)
    print(
        f"Los días entre {fecha[0]}/{fecha[1]}/{fecha[2]}",
        f"y {fecha2[0]}/{fecha2[1]}/{fecha2[2]} son {dif}.",
    )
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
