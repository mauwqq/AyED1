"""
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo.
"""

import random as rn


def pedir_numero() -> int:
    while True:
        try:
            n = int(input("Ingrese la cantidad de naranjas cosechadas: "))
            if n > 0:
                break
            print("Ingrese un numero positivo.")
        except ValueError:
            print("Debe ingresarse un numero.")
    return n


def gen_peso_naranjas(naranjas: int) -> tuple[int]:
    """Hace una tupla con el pesos generado de cada naranja y los devuelve.
    Pre -> Recibe la cantidad de naranjas.
    Post -> Devuelve una tupla con numeros entre el 150 al 350 para cada naranja.
    """
    return (rn.randint(150, 350) for _ in range(naranjas))


def calc_jugo(peso_naranjas: tuple) -> int:
    """usa sum() para sumar 1 cada vez que encuentre un valor > 300 o < 200 en peso_naranjas.
    Pre -> Recibe la tupla de los pesos de las naranjas.
    Post -> Retorna un entero.
    """
    return sum(1 for peso in peso_naranjas if peso > 300 or peso < 200)


def calc_cajones(peso_naranjas: tuple) -> tuple[int, float]:
    """Calcula la cantidad de cajones llenos y cuantas naranjas sobran si sobra  alguna.
    Pre -> Recibe una tupla de enteros con los pesos de cada naranja.
    Post -> Devuelve una tupla con la cantidad de cajones y de cuantas naranjas quedaron
    de resto, que no llegaron a llenar un cajon.
    """
    cajones = len(peso_naranjas) // 100
    resto = len(peso_naranjas) % 100
    return cajones, resto


def calc_peso_cajones(peso_naranjas: tuple) -> list[float]:
    """Agrupa los pesos de las naranjas en cajones de 100 naranjas.
    Pre -> Recibe una tupla de enteros con el peso de cada naranja.
    Post -> Devuelve el peso de los cajones.
    """
    peso_cajones = []
    acumulador = 0
    for i, peso in enumerate(peso_naranjas):
        acumulador += peso
        if i % 100 == 0 or i == len(peso_naranjas):
            peso_cajones.append(acumulador)
            acumulador = 0
    return peso_cajones


def calc_camiones(peso_cajones: tuple) -> tuple[int, float]:
    """Calcula cuantos camiones se van a necesitar y si se aprueba su viaje.
    Pre -> Recibe el peso de los cajones.
    Post -> Devuelve la cantidad de camiones que van a viajar y si hay,
    la cantidad de gramos de naranjas para el proximo viaje.
    """
    camiones = 1
    acumulador = 0
    resto = 0
    capacidad_camion = 500000  # 500kg
    for peso in peso_cajones:
        acumulador += peso
        if acumulador >= capacidad_camion:
            camiones += 1
            acumulador = 0
    if acumulador > 0:
        porcentaje = (acumulador / capacidad_camion) * 100
        if porcentaje >= 80:
            camiones += 1
        else:
            resto = (porcentaje / 100) * capacidad_camion

    return camiones, resto


def imprimir_resultado(datos):
    cajones, naranjas_jugo, resto_naranjas, camiones, resto_camiones = (
        datos  # desempaqueto
    )
    print(f"La cantidad de cajones es de: {cajones}")
    print(f"La cantidad de naranjas para jugo es de: {naranjas_jugo}")
    print(f"La cantidad de naranjas sobrantes es de: {resto_naranjas}")
    if camiones > 0:
        print(f"Se utilizaran {camiones} camiones.")
        if resto_camiones > 0:
            print(
                f"Queda para el proximo viaje {resto_camiones:.2f} gramos de naranjas."
            )
    else:
        print(
            "No se llego al minimo del 80% de ocupacion por lo que no se despachara ningun camion."
        )


def main():
    naranjas_cosechadas = pedir_numero()
    peso_naranjas = gen_peso_naranjas(naranjas_cosechadas)
    naranjas_jugo = calc_jugo(peso_naranjas)
    cajones, resto_cajones = calc_cajones(peso_naranjas)
    peso_cajones = calc_peso_cajones(peso_naranjas)
    camiones, resto = calc_camiones(peso_cajones)
    datos = (cajones, naranjas_jugo, resto_cajones, camiones, resto)
    imprimir_resultado(datos)


if __name__ == "__main__":
    main()
