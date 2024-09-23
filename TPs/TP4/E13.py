"""
Muchas aplicaciones financieras requieren que los números sean expresados tam-
bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
cincuenta y tres". Escribir un programa que utilice una función para convertir un
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
la función si también aceptara números negativos? ¿Y números con decimales?
"""

unidades = [
    "",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
]
decenas = [
    "",
    "",
    "veinte",
    "veintiuno",
    "veintidós",
    "veintitrés",
    "veinticuatro",
    "veinticinco",
    "veintiséis",
    "veintisiete",
    "veintiocho",
    "veintinueve",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
]
centenas = [
    "",
    "cien",
    "doscientos",
    "trescientos",
    "cuatrocientos",
    "quinientos",
    "seiscientos",
    "setecientos",
    "ochocientos",
    "novecientos",
]


def pedir_numero() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input("Ingrese un número positivo: "))
            if n >= 0:  # Cambiado a >= 0 para permitir cero.
                break
            print("El número tiene que ser positivo o cero.")
        except ValueError:
            print("Debe ingresar un número.")
    return n


def convertir_hasta_miles(n: int) -> str:
    """Convierte números hasta mil.

    Pre: n es un entero que representa un número menor a 1000.

    Post: Retorna la representación en letras del número.

    """
    if n < 100:
        return (
            unidades[n]
            if n < 20
            else decenas[n // 10] + (" y " + unidades[n % 10] if n % 10 != 0 else "")
        )
    elif n < 1000:
        return centenas[n // 100] + (
            " " + convertir_hasta_miles(n % 100) if n % 100 != 0 else ""
        )
    elif n == 1000:
        return "mil"
    else:
        return "mil " + convertir_hasta_miles(n % 1000)


def convertir_a_letras(numero: int) -> str:
    """Convierte un número entero entre 0 y 1 billón a su representación en letras.

    Pre: numero es un entero entre 0 y 1.000.000.000.000.

    Post: Retorna la representación en letras del número.

    """
    if numero < 0:
        return "menos " + convertir_a_letras(-numero)
    if numero == 0:
        return "cero"
    partes = []
    if numero >= 1000000:
        millones = numero // 1000000
        partes.append(convertir_hasta_miles(millones) + " millones")
        numero %= 1000000
    if numero >= 1000:
        miles = numero // 1000
        partes.append(convertir_hasta_miles(miles) + " mil")
        numero %= 1000
    if numero > 0:
        partes.append(convertir_hasta_miles(numero))
    return " ".join(partes).strip()


def main() -> None:
    numero = int(input("Ingrese un número entre 0 y 1 billón: "))
    if 0 <= numero <= 1000000000000:
        letras = convertir_a_letras(numero)
        print(f"El número {numero} se escribe como: {letras}.")
    else:
        print("El número debe estar en el rango de 0 a 1 billón.")


if __name__ == "__main__":
    main()
