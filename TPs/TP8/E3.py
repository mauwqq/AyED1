"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""

from typing import Tuple
import re


def input_mail() -> str:
    """Asks the user for input and returns it

    Pre: None.

    Post: returns the user input in a string.

    """
    return input("Ingrese el mail: ")


def valid_mail(mail: str) -> bool:
    """Checks the validity of the mail.

    Pre: mail is a string.

    Post: Returns True if the mail matches with the regex.
          Returns False if the mail doesn't matches with the regex.

    """
    return bool(re.match(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", mail))


def dissasembly_mail(mail: str) -> Tuple[str]:
    """Divides the mail into pieces and returns them in a tuple.

    Pre: mail is a string.

    Post: If the mail is valid returns it splitted into a tuple
          Example: local@domain.com.ar = (local, domain, com, ar)
          If the mail is invalid returns a empty tuple.

    """
    if not valid_mail(mail):
        return ()
    local, domain = mail.split("@")
    return local, *domain.split(".")


def main() -> None:
    """Main function of the program"""
    mail_parts = dissasembly_mail(input_mail())
    if not mail_parts:
        print("El mail ingresado es invalido")
    else:
        print(mail_parts)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
