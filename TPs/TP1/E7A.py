"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
"""

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


def pedir_fecha() -> list[int]:
    fecha = list()
    texto = ["Año", "Mes", "Dia"]
    print("Ingrese la fecha")
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
                else:
                    print("El numero ingresado debe ser positivo.")
            except ValueError:
                print("Debe ingresar un numero, reintentar.")
    return fecha


def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def comprobar_mes(mes: int) -> bool:
    return mes <= len(meses.keys())


def comprobar_dia(dia: int, mes: int) -> bool:
    return dia <= meses.get(mes)


def pedir_cuanto_adelantar() -> int:
    while True:
        try:
            num = int(input("cuantos dias quiere sumar a la fecha: "))
            if num > 0:
                break
            else:
                print("El numero ingresado debe ser positivo.")
        except ValueError:
            print("Debe ingresar un numero, reintentar.")
    return num


def diasiguiente(dia: int, mes: int, anio: int) -> tuple[int]:
    if (dia + 1) > meses.get(mes):
        if mes != 12:
            mes += 1
            dia = 1
        else:
            anio += 1
            mes = 1
            dia = 1
    else:
        dia += 1
    return dia, mes, anio


def calcular_fecha(adelanto: int, dia: int, mes: int, anio: int) -> tuple[int]:
    i = 0
    while i < adelanto:
        dia, mes, anio = diasiguiente(dia, mes, anio)
        i += 1
    return dia, mes, anio


def main():
    anio, mes, dia = pedir_fecha()
    print(f"La fecha es: {dia}/{mes}/{anio}")
    adelanto = pedir_cuanto_adelantar()
    dia, mes, anio = calcular_fecha(adelanto, dia, mes, anio)
    print(f"{adelanto} dias despues: {dia}/{mes}/{anio}")


if __name__ == "__main__":
    main()
