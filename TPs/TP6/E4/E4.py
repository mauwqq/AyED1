"""
Desarrollar un programa para eliminar todos los comentarios de un programa es-
crito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
bles) y que también se considera comentario a las cadenas de documentación
(docstrings).
"""

import re


def leer_archivo(ruta: str) -> str:
    """Abre el archivo pasado como parametro y lo devuelve como string.

    Pre: ruta es un string que tiene la ruta del archivo a operar.

    Post: Devuelve un string con todo lo que contiene el archivo.

    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"El archivo {ruta} no existe")
        return ""


def eliminar_comentarios(archivo: str) -> str:
    """Utilizando expresiones regulares elimina los caracteres desde un # hasta el final de la linea.
    Asi como los bloques entre los que hayan '""" """'.
    
    Pre: Recibe archivo, un string, el que se va a modificar.
    
    Post: Devuelve el archivo con las modificaciones correspondientes.
    
    """
    # La flag re.DOTALL permite que se seleccione varias lineas, para agarrar un bloque.
    # ^s* hace que coincida si antes de las """ o # hay solo espacios en blanco.
    archivo = re.sub(
        r'^\s*""".*?"""', "", archivo, flags=re.DOTALL | re.MULTILINE
    ).strip()
    # La flag re.MULTILINE permite que se seleccione desde el '#' hasta el final de la linea con el patron especificado '$'
    archivo = re.sub(r"^\s*#.*$", "", archivo, flags=re.MULTILINE).strip()
    return archivo


def main() -> None:
    """Función principal del programa."""
    archivo = leer_archivo("test.py")
    archivo_modif = eliminar_comentarios(archivo)
    print(archivo_modif)
    return None


if __name__ == "__main__":
    main()
