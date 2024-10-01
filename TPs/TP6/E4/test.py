"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta.
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes.
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""

from typing import List,Tuple, Dict


def pedir_string(msj: str) -> str:
    """Pide al usuario que ingrese un texto y lo devuelve.

    Pre: msj es un string, el mensaje que se va a mostrar para el input.

    Post: Devuelve un string.

    """
    return input(msj)


def pedir_alturas() -> float:
    """Pide un numero flotante y lo devuelve si es positivo o -1.

    Pre: No recibe nada.

    Post: Devuelve n un numero flotante.

    """
    while True:
        try:
            n = float(input("Ingrese la altura del atleta: "))
            if n == -1.0:
                break
            if n > 0.0:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un numero positivo o -1.")
    return n


def registrar_atletas() -> List[Tuple[str, float]]:
    """Pide inputs de deportes y alturas de atletas de esos deportes
    para anotarlos en una lista del formato lista = [(deporte, altura)...].

    Pre: No recibe nada.

    Post: Devuelve una lista de tuplas con el formato mencionado.

    """
    atletas = []
    while True:
        deporte = pedir_string("Ingrese el deporte (-1 para salir): ")
        if deporte == "-1": 
            break
        while True:
            altura = pedir_alturas()
            if altura == -1.0:
                break
            atletas.append((deporte, altura))
    return atletas

#hola
def pasar_a_dict(atletas_l: List[Tuple[str, float]]) -> Dict[str, List[float]]:
    """convierte la lista de tuplas a un diccionario de deportes y alturas para
    que sea mas facil de manipular.

    Pre: Recibe atletas_l, una lista de tuplas, cada tupla tiene un string y un flotante.

    Post: Devuelve un diccionario que tiene una clave por cada deporte ingresado y
          cada deporte tiene una lista de las alturas en flotante.

    """
    return {deporte: [altura for _, altura in atletas_l if _ == deporte]for deporte, _ in set(atletas_l)}


def grabar_rango_alturas(ruta: str, atletas: Dict[str, List[float]]) -> None:
    """Escribe los deportes y sus respectivas alturas en el formato indicado.

    Pre: ruta es un string que representa la ruta del .txt sobre el cual
         open() va a escribir.
         atletas es un diccionario, cada clave es un deporte y su valor es una
         lista de alturas en flotantes.

    Post: """
    with open(ruta, 'w', encoding='utf-8') as f: #hola
        for deporte, alturas in atletas.items():
            f.write(f"""{deporte}\n{"\n".join(str(altura) for altura in alturas)}\n""")
    return None


def leer_archivo(ruta: str) -> Dict[str, List[float]]:
    """Lee el archivo que se le de como parametro y lo formatea como un
    diccionario.

    Pre: ruta es la ruta del archivo a abrir, en formato string.

    Post: Devuelve un diccionario que tiene una clave por cada deporte ingresado y
          cada deporte tiene una lista de las alturas en flotante.

    """
    atletas = {}
    with open(ruta, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if line.isalpha():
                deporte = line
                atletas.setdefault(deporte, [####])
            else:
                atletas[deporte].append(float(line))
    return atletas


def grabar_promedio() -> None:
    """Escribe el archivo grabar_rango_altura con los deportes y cada altura de
    atleta separado por un newline(\n).

    Pre: No recibe nada.

    Post: No devuelve nada.

    """
    atletas = leer_archivo("grabar_rango_altura.txt")
    with open("grabar_promedio.txt", 'w', encoding='utf-8') as f:
        for deporte, altura in atletas.items():
            f.write(f"{deporte}\n{sum(altura) / len(altura):.2f}\n")
    return None


def mostrar_mas_altos() -> None:
    """Muestra por pantalla los deportes cuyos atletas tienen un promedio de altura
    superior al promedio general de todos los deportes.

    Pre: No recibe parámetros. Lee los datos de "grabar_promedio.txt", que contiene
         los deportes y sus promedios de alturas.

    Post: Muestra por pantalla los deportes que superan el promedio general de altura,
          en caso de que existan, o un mensaje indicándolo.

    """
    atletas = leer_archivo("grabar_promedio.txt")
    if not atletas:
        print("No hay datos de atletas.")
        return None
    total_promedios = sum(sum(alturas) / len(alturas) for alturas in atletas.values())
    cantidad_deportes = len(atletas)
    promedio_general = total_promedios / cantidad_deportes if cantidad_deportes > 0 else 0
    print(f"El promedio general es: {promedio_general:.2f}")
    deportes_mas_altos = [deporte for deporte, alturas in atletas.items() if (sum(alturas) / len(alturas)) > promedio_general]
    if deportes_mas_altos:
        print("Disciplinas cuyos atletas superan el promedio general:")
        for deporte in deportes_mas_altos:
            promedio_deporte = sum(atletas[deporte]) / len(atletas[deporte])
            print(f"{deporte}: {promedio_deporte:.2f}")
    else:
        print("Ningún deporte tiene un promedio superior al promedio general.")
    return None


def main() -> None:
    """Función principal del programa."""
    atletas_l = registrar_atletas()
    atletas = pasar_a_dict(atletas_l)
    grabar_rango_alturas("grabar_rango_altura.txt", atletas)
    grabar_promedio()
    mostrar_mas_altos()


if __name__ == '__main__':
    main()
