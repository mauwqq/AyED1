/*
En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi-
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función.
*/


fn is_orthogonal(a: (i8, i8), b: (i8, i8)) -> bool {
    if (a.0 * b.0) + (a.1 * b.1) == 0 {
        true
    } else {
        false
    }
}

fn main() {
    let a:(i8, i8) = (2,3);
    let b:(i8, i8) = (-3,2);
    match is_orthogonal(a, b) {
        true => println!("Son ortogonales."),
        false => println!("No son ortogonales."),
    }
}