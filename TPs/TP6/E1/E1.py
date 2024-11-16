"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe  –> ITALIA.TXT
Pérez, Juan        –> ESPAÑA.TXT
Smith, John        –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""

from typing import List

patron = {"ian": "armenia", "ini": "italia", "ez": "españa"}


def cargar_data(ruta: str) -> List[str]:
    """Abre el archivo de texto en solo lectura, lo divide por linea,
    y lo devuelve en una lista.

    Pre: ruta es un string, la ruta del archivo a abrir.

    Post: Devuelve una lista de strings con los datos del archivo.

    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return [line.strip("\n") for line in archivo]
    except FileNotFoundError:
        print("El archivo no fue encontrado.")


def guardar_data(archivo: str, apellido_nombre: str) -> None:
    """Abre el archivo del pais donde se van a guardar los datos,
    escribe los datos y devuelve None.

    Pre: archivo es un string, el nombre que va a tener el archivo
         a ser creado/actualizado.

    Post: Termina de añadir los datos y devuelve None.

    """
    with open(f"{archivo.upper()}.txt", "a", encoding="utf-8") as file:
        file.write(apellido_nombre + "\n")
    return None


def dividir_en_archivos(apellidos: List[str]) -> None:
    """Itera sobre los apellidos buscando las letras con las que termina para llamar
    a guardar_data para ubicarlos en su respectivo archivo de texto.

    Pre: apellidos es una lista de strings con nombres y apellidos.

    Post: No devuelve nada.

    """
    for elem in apellidos:
        apellido = elem.split(", ", 1)[0].lower()
        if apellido.endswith("ian"):
            guardar_data(patron["ian"], elem)
        elif apellido.endswith("ini"):
            guardar_data(patron["ini"], elem)
        elif apellido.endswith("ez"):
            guardar_data(patron["ez"], elem)
    return None


def main() -> None:
    """Función principal del programa."""
    apellidos = cargar_data("apellidos.txt")
    dividir_en_archivos(apellidos)


if __name__ == "__main__":
    main()

# End-of-file (EOF)
