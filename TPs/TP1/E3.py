"""
Una persona desea llevar el control de los gastos realizados al viajar en el
subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza
un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se
solicita desarrollar una función que reciba como parámetro la cantidad de
viajes realizados en un determinado mes y devuelva el total gastado en viajes.
Realizar también un programa para verificar el comportamiento de la función.
"""


def pedir_numero(msj: str) -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                break
            print("El número tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def calcular_pasaje(viajes: int, importe: int) -> tuple[float]:
    """Calcula el descuento de los pasajes y los devuelve.

    Pre: Recibe la cantidad de viajes como entero positivo.
         Recibe el precio de esos viajes como entero positivo.

    Post: Devuelve el importe con descuento y el descuento en una tupla de
          flotantes.

    """
    importe_final = 0
    desc = 0.0
    if viajes <= 20:
        importe_final = -1
    elif viajes <= 30:
        desc = 0.20
    elif viajes <= 40:
        desc = 0.30
    else:
        desc = 0.40
    if importe_final != -1:
        importe_final = importe - (importe * desc)
    return importe_final, desc


def imprimir_resultado(viajes: int, importe_final: int, desc: float) -> None:
    """Imprime un resumen del descuento aplicado y el importe total calculado.
    Muestra al usuario el total de viajes, el porcentaje de descuento aplicado
    y el importe final a pagar. Si el importe final es -1, se indica que se debe
    consultar el valor actualizado en Internet.

    Pre: Recibe viajes como entero positivo.
         Recibe importe_final como entero positivo o -1 si no esta disponible.
         Recibe desc en número flotante.

    Post: Si importe_final no es -1 imprime el resumen.
          Si importe_final es -1 informa que averigue el precio en internet.

    """
    if importe_final != -1:
        print(
            f"El total de viajes fue: {viajes}",
            f"Se le aplico un descuento del {desc*100:.0f}%",
            f"El importe final es de ${importe_final}",
            sep="\n",
        )
    else:
        print("Averiguar en Internet el valor actualizado.")


def main() -> None:
    viajes = pedir_numero("Ingrese la cantidad de viajes: ")
    importe = pedir_numero("Ingrese el importe total: ")
    importe_final, desc = calcular_pasaje(viajes, importe)
    imprimir_resultado(viajes, importe_final, desc)


if __name__ == "__main__":
    main()
