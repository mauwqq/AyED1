"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
"""


def pedir_string() -> str:
    """Solicita al usuario que ingrese un texto y lo devuelve.

    Post: Retorna la cadena de texto ingresada por el usuario.
    
    """
    return input("Ingrese el texto: ")


def ordenar(cadena: str) -> str:
    """Ordena las palabras de una cadena según su longitud, conservando la puntuación.

    Pre: cadena es una cadena de texto con palabras separadas por espacios.
    
    Post: Retorna una nueva cadena con las palabras ordenadas por longitud.
    
    """
    palabras = cadena.split()
    palabras_con_puntuacion = [
        (palabra, ''.join([x for x in palabra if x.isalnum()])) for palabra in palabras
    ]
    palabras_ordenadas = sorted(palabras_con_puntuacion, key=lambda x: len(x[1]))
    return ' '.join(palabra[0] for palabra in palabras_ordenadas)


def main() -> None:
    cadena = pedir_string()
    print(ordenar(cadena))


if __name__ == '__main__':
    main()
