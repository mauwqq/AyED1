"""
Se solicita crear un programa para leer direcciones de correo electrónico y
verificar si representan una dirección válida. Por ejemplo
usuario@dominio.com.ar. Para que una dirección sea considerada válida el nombre
de usuario debe poseer solamente caracteres alfanuméricos, la dirección contener
un solo carácter @, el dominio debe tener al menos un carácter y tiene que
finalizar con .com o .com.ar. Repetir el proceso de validación hasta ingresar
una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin
repetirlos y ordenados alfabéticamente, recordando que las direcciones de mail
no distinguen mayúsculas ni minúsculas.
"""

import re


def pedir_mail() -> str:
    """Pide al usuario que ingrese un mail y lo devuelve.
    
    Pre: No recibe nada.
    
    Post: Devuelve un string.
    
    """
    return input("Ingrese una dirección de correo electrónico (o presione Enter para finalizar): ")


def es_email_valido(email: str) -> bool:
    """Verifica si una dirección de correo electrónico es válida.
    La condicion busca una cadena de caracteres mayúsculas o minúsculas y numeros
    seguido de un "@" y de otro string de mayúsculas o minúsculas y numeros si
    finaliza en .com o .com.ar.

    Pre: email es una cadena de caracteres.

    Post: Devuelve True si el correo es válido, de lo contrario False.

    """
    patron = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$"
    return re.match(patron, email) is not None


def main() -> None:
    """Función principal del programa."""
    correos = []
    while True:
        email = pedir_mail()
        if not email:
            break
        if es_email_valido(email):
            correos.append(email.lower())
        else:
            print("Dirección de correo inválida. Intente nuevamente.")
    if not correos:
        print("No se encontraron correos validos.")
    else:
        dominios = sorted(set(email.split("@")[1] for email in correos))
        print("\nDominios válidos (sin repetir):")
        print("\n".join("".join(dominio) for dominio in dominios))
    return None


if __name__ == "__main__":
    main()
