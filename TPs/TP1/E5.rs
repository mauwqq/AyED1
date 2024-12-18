/*
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem-
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y de-
vuelven True o False. No se permite utilizar ayudas externas a las mismas.
*/
use std::io;


fn ask_input(message: String) -> u64 {
    loop {
        let mut input: String = String::new();
        println!("{}", message);
        io::stdin().read_line(&mut input).expect("No se pudo leer el input.");
        match input.trim().parse::<u64>() {
            Ok(num) => {
                if num > 0 {
                    return num;
                } else {
                    println!("Debe ingresar un numero positivo.");
                }
            },
            Err(_) => {
                println!("Debe ingresar un numero.");
            }
        };
    }
}

fn main() {
    let oblongo = |x: u64| {
        (1..=(x as f64).sqrt() as u64 + 1)
            .any(|n| x == n * (n + 1))
    };
    let triangular = |x: u64| {
        (1..=((2 * x) as f64).sqrt() as u64)
            .any(|n| n * (n + 1) / 2 == x)
    };
    let n_oblongo: u64 = ask_input("Ingresa el numero para comprobar si es oblongo: ".to_string());
    if oblongo(n_oblongo) {
        println!("El numero {} es oblongo.", n_oblongo);
    } else {
        println!("El numero {} no es oblongo.", n_oblongo);
    }
    let n_triangular: u64 = ask_input("Ingresa el numero para comprobar si es triangular: ".to_string());
    if triangular(n_triangular) {
        println!("EL numero {} es triangular.", n_triangular);
    } else {
        println!("El numero {} no es triangular", n_triangular);
    }
}