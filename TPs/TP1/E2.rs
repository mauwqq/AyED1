/*
-*- coding: utf-8 -*-
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
*/
use std::io;

struct Date(u16, u16, u16);

fn input_number(message: &str) -> u16 {
    let mut input = String::new();
    println!("{}: ", message);
    io::stdin()
        .read_line(&mut input)
        .expect("No se pudo leer la entrada.");
    let input: u16 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Entrada no valida, se usará 0 por defecto");
            0
        }
    };
    input
}

fn is_leap(year: u16) -> bool {
    (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
}

fn check_date(date: &Date) -> bool {
    let mut months: [[u16; 2]; 12] = [
        [1, 31],
        [2, 28],
        [3, 31],
        [4, 30],
        [5, 31],
        [6, 30],
        [7, 31],
        [8, 31],
        [9, 30],
        [10, 31],
        [11, 30],
        [12, 31],
    ];
    if is_leap(date.2) {
        months[1][1] = 29;
    }
    if date.1 < 1 || date.1 > 12 {
        return false;
    }
    return date.0 <= months[(date.1 - 1) as usize][1];
}

fn main() {
    let day = input_number("Introduce el dia");
    let month = input_number("Introduce el mes");
    let year = input_number("Introduce el año");
    let date = Date(day, month, year);
    if check_date(&date) {
        println!("La fecha es valida.");
    } else {
        println!("La fecha es invalida");
    }
}
