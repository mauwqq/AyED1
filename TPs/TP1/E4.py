"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""


def solicitar_valor(msj: str) -> int:
    while True:
        try:
            valor = int(input(msj))
            if valor <= 0:
                print("Ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Valor inválido, reintentar.")


def recibir_valores() -> tuple[int, int]:
    while True:
        total_compra = solicitar_valor("Ingrese el monto total de la compra: ")
        dinero_recibido = solicitar_valor("Ingrese el dinero recibido: ")
        if dinero_recibido >= total_compra:
            return total_compra, dinero_recibido
        else:
            print("El dinero recibido no es suficiente.")


def calcular_cambio(total: int, recibido: int) -> tuple[int, int, int, int, int, int, int, int, int]:
    if recibido == total:
        # No hay cambio
        return 0, 0, 0, 0, 0, 0, 0, 0, 0

    vuelto = recibido - total
    b_5000 = vuelto // 5000
    resto = vuelto % 5000
    b_1000 = resto // 1000
    resto = resto % 1000
    b_500 = resto // 500
    resto = resto % 500
    b_200 = resto // 200
    resto = resto % 200
    b_100 = resto // 100
    resto = resto % 100
    b_50 = resto // 50
    resto = resto % 50
    b_10 = resto // 10
    resto = resto % 10
    return vuelto, resto, b_5000, b_1000, b_500, b_200, b_100, b_50, b_10


def imprimir_resultado(compra: int, recibido: int, vuelto: int, resto: int, b_5000: int, b_1000: int, b_500: int, b_200: int, b_100: int, b_50: int, b_10: int) -> None:
    billetes = [
        ("Billetes de 5000", b_5000),
        ("Billetes de 1000", b_1000),
        ("Billetes de 500", b_500),
        ("Billetes de 200", b_200),
        ("Billetes de 100", b_100),
        ("Billetes de 50", b_50),
        ("Billetes de 10", b_10)
        ]
    if resto != 0:
        print("el cambio no puede entregarse debido a falta de billetes con denominaciones adecuadas.")
    else:
        print(f"La compra fue de: ${compra}")
        print(f"El monto recibido fue de: ${recibido}")
        if vuelto == 0:
            print("No hay vuelto.")
        else:
            print(f"El vuelto es de: ${vuelto}")
            print("-"*50)
            for texto, valor in billetes:
                if valor > 0:
                    print(f"{texto}: {valor}")


def main() -> None:
    total_compra, dinero_recibido = recibir_valores()
    vuelto, resto, b_5000, b_1000, b_500, b_200, b_100, b_50, b_10 = calcular_cambio(total_compra, dinero_recibido)
    imprimir_resultado(total_compra, dinero_recibido, vuelto, resto, b_5000, b_1000, b_500, b_200, b_100, b_50, b_10)


if __name__ == '__main__':
    main()
