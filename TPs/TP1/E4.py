"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa
que le indique al cajero el cambio que debe entregarle al cliente. Para eso
se ingresan dos números enteros, correspondientes al total de la compra y al
dinero recibido. Informar cuántos billetes de cada denominación deben ser
entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10.
Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el
cambio no pudiera entregarse debido a falta de billetes con denominaciones
adecuadas. Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto
debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200,
1 billete de $100 y 3 billetes de $10.
"""

billetes = {
    "billetes 5000": 0,
    "billetes 1000": 0,
    "billetes 500": 0,
    "billetes 200": 0,
    "billetes 100": 0,
    "billetes 50": 0,
    "billetes 10": 0,
}


def solicitar_valor(msj: str) -> int:
    """Solícita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string que se va a mostrar al usuario como mensaje para
         ingresar el número.

    Post: Devuelve el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            valor = int(input(msj))
            if valor > 0:
                return valor
            print("Ingrese un número positivo.")
        except ValueError:
            print("Valor inválido, reintentar.")


def recibir_valores() -> tuple[int]:
    """Solicita al usuario el monto total de una compra y el dinero recibido, y
    válida que el dinero recibido sea suficiente.

    Post: Devuelve una tupla (total_compra, dinero_recibido) si el dinero es
          suficiente.

    """
    while True:
        total_compra = solicitar_valor("Ingrese el monto total de la compra: ")
        dinero_recibido = solicitar_valor("Ingrese el dinero recibido: ")
        if dinero_suficiente(total_compra, dinero_recibido):
            return total_compra, dinero_recibido
        print("El dinero recibido no es suficiente.")


def dinero_suficiente(total_compra: int, dinero_recibido: int) -> bool:
    """Verifica que el dinero recibido no sea menor al total de la compra.

    Pre: total_compra es un número entero positivo.
         dinero_recibido es un número entero positivo.

    Post: Devuelve True si el dinero recibido es mayor o igual al total de la
          compra.
          Devuelve False si el dinero recibido no es mayor o igual al total de
          la compra.

    """
    return dinero_recibido >= total_compra


def calcular_cambio(total: int, recibido: int) -> tuple[int]:
    """Calcula cuantos billetes de cada denominacion necesita darle al
    usuario.

    Pre: total es un numero entero positivo.
         recibido es un numero entero positivo.

    Post: Realiza las cuentas necesarias y devuelve una tupla(vuelto, resto)
          con el cambio y el resto si quedo dinero que no se puede dar por falta
          de billetes.

    """
    if recibido == total:
        # No hay cambio
        return 0, 0
    vuelto = recibido - total
    billetes.update({"billetes 5000": vuelto // 5000})
    resto = vuelto % 5000
    billetes.update({"billetes 1000": resto // 1000})
    resto = resto % 1000
    billetes.update({"billetes 500": resto // 500})
    resto = resto % 500
    billetes.update({"billetes 200": resto // 200})
    resto = resto % 200
    billetes.update({"billetes 100": resto // 100})
    resto = resto % 100
    billetes.update({"billetes 50": resto // 50})
    resto = resto % 50
    billetes.update({"billetes 10": resto // 10})
    resto = resto % 10
    return vuelto, resto


def imprimir_resultado(compra: int, recibido: int, vuelto: int, resto: int) -> None:
    """Imprime el resultado de las cuentas anteriores, si hay cambio, si hay
    billetes y si no alcanza.

    Pre: compra es un entero positivo.
         recibido es un entero positivo.
         vuelto es un entero positivo.
         resto es un entero positivo.

    Post: Si no hay billetes con las denominaciones necesarias lo imprime.
          Si no, imprime un resumen de la cuenta y si hay vuelto tambien.

    """
    if resto:
        print(
            "El cambio no puede entregarse debido a falta de billetes con",
            "denominaciones adecuadas.",
        )
    else:
        print(f"La compra fue de: ${compra}")
        print(f"El monto recibido fue de: ${recibido}")
        if not vuelto:
            print("No hay vuelto.")
        else:
            print(f"El vuelto es de: ${vuelto}")
            print("-" * 50)
            for texto, valor in billetes.items():
                if valor > 0:
                    print(f"Billetes de {texto.split(" ")[1]}: {valor}")


def main() -> None:
    total_compra, dinero_recibido = recibir_valores()
    vuelto, resto = calcular_cambio(total_compra, dinero_recibido)
    imprimir_resultado(total_compra, dinero_recibido, vuelto, resto)


if __name__ == "__main__":
    main()
