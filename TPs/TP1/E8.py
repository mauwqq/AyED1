"""
La siguiente función permite averiguar el día de la semana para una fecha determi-
nada. La fecha se suministra en forma de tres parámetros enteros y la función de-
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
"""


dias = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado"
}


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


def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def pedir_fecha() -> tuple[int]:
    fecha = []
    while not fecha[1:]:
        try:
            mes = int(input("Ingrese el mes: "))
            if (mes <= 0) or (mes > 12):
                print("Ingrese un mes valido.")
            else:
                fecha.append(mes)
                anio = int(input("Ingrese el anio: "))
                if es_bisiesto(anio):
                    meses[2] = 29
                if anio > 0:
                    fecha.append(anio)
        except ValueError:
            print("Debe ingresar un numero")
    return fecha


def dia_de_la_semana(q: int, m: int, anio: int) -> int:
    """Usando la congruencia de Zeller para el calendario Gregoriano
       calcula el dia de la semana.
    Pre -> recibe el dia, mes y año en numeros enteros
    """
    if m < 3:
        m += 10
        anio -= 1
    else:
        m -= 2
    j = anio // 100
    k = anio % 100
    h = (((26*m-2)//10)+q+k+(k//4)+(j//4)-(2*j))%7
    return h


def imprimir_calendario(mes: int, anio: int) -> None:
    for i in range(1,meses.get(mes)+1):
        dia = dia_de_la_semana(i, mes, anio)
        if dia == 0:
            print("-"*25)
        print(f"{i}: {dias.get(dia)}")


def main() -> None:
    mes, anio = pedir_fecha()    
    imprimir_calendario(mes, anio)


if __name__ == '__main__':
    main()
