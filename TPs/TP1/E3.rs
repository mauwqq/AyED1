/*
Una persona desea llevar el control de los gastos realizados al viajar en el subte-
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es-
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
llar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un pro-
grama para verificar el comportamiento de la función.
1 a 20 => Averiguar en internet el precio actualizado.
21 a 30 => 20%
31 a 40 => 30%
40+ => 40%
*/
use std::io;

fn user_input(message: String) -> u8 {
    loop {
        let mut n = String::new();
        println!("{}", message);
        io::stdin().read_line(&mut n).expect("No se pudo leer el input.");
        match n.trim().parse() {
            Ok(value) => {
                if value > 0 {
                    return value;
                } else {
                    println!("Debe ingresar un numero positivo.");
                }
            },
            Err(_) => {
                println!("Valor invalido, vuelva a intentarlo.");
            }
        };
    }
}

fn calculate(n: u8) {
    match n {
        1..=20 => println!("Averiguar en internet el precio actualizado."),
        21..=30 => println!("20% de descuento sobre tarifa máxima."),
        31..=40 => println!("30% de descuento sobre tarifa máxima."),
        _ => println!("40% de descuento sobre tarifa máxima."),
    }
}

fn main() {
    let n: u8 = user_input("Ingrese cuantos viajes realizo este mes: ".to_string());
    calculate(n);
}