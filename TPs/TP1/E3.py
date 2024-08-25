"""
Una persona desea llevar el control de los gastos realizados al viajar en el subte-
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es-
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
llar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un pro-
grama para verificar el comportamiento de la función.
"""


def pedir_numero(msj: str) -> int:
    """Recibe un mensaje, lo muestra, guarda y retorna un numero entero positivo
    Pre -> recibe un string, el mensaje que va a mostrar el input para recibir
           el numero.
    Post -> Retorna el valor ingresado si es un numero entero positivo.
    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                break
            print("El numero tiene que ser positivo.")
        except ValueError:
            print("Debe ingresar un numero.")
    return n


def calcular_pasaje(viajes: int, importe: int) -> tuple[float]:
    """Calcula el descuento de los pasajes y los devuelve
    Pre -> recibe la cantidad de viajes como entero positivo,
           recibe el precio de esos viajes como entero positivo.
    Post -> devuelve el importe con descuento y el descuento en,
            una tupla de flotantes.
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
